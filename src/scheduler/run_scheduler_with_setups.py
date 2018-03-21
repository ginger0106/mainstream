
import argparse
import datetime
import csv
import fnmatch
import scheduler_util
import os
import sys

sys.path.append('data')
import app_data_mobilenets as app_data

sys.path.append('src/scheduler')
import run_scheduler as sched
import run_scheduler_simulator as sim

sys.path.append('src/scheduler/types')
import Scheduler
import Setup

def get_args(simulator=True):
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num_apps_range", required=True, type=int)
    parser.add_argument("-o", "--outdir", required=True)
    parser.add_argument("-r", "--run_id", required=True)
    parser.add_argument("-v", "--verbose", type=int, default=0)
    parser.add_argument("-f", "--setups_file")
    parser.add_argument("-m", "--metric", default="f1")
    parser.add_argument("-s", "--simulator", type=int, default=0)
    parser.add_argument("-t", "--scheduler_type", default="greedy")
    return parser.parse_args()

def get_eval(entry_id, s, stats, budget, latency_us, metric_key="metric"):
    print metric_key
    row = [
        entry_id,
        stats[metric_key],
    ]
    row += stats["frozen"]
    row += stats["fps"]
    row += [budget]
    row += [latency_us]
    return row

def run_scheduler(metric, setup, setup_suffix, scheduler_type, is_simulator):

    apps = [app.to_map() for app in setup.apps]
    budget = setup.budget

    s = Scheduler.Scheduler(metric,
                            apps,
                            setup.video_desc.to_map(),
                            app_data.model_desc,
                            0,
                            scheduler=scheduler_type)

    # Run mainstream
    start = datetime.datetime.now()
    if (is_simulator):
        print "Running " + scheduler_type + " simulator."

        s, stats = sim.run_simulator(metric,
                                     apps,
                                     setup.video_desc.to_map(),
                                     budget,
                                     scheduler=scheduler_type)
    else:
        print "Running " + scheduler_type + " with streamer."

        if scheduler_type == "greedy" or scheduler_type == "hifi":
            sharing_type = "mainstream"
        else:
            sharing_type = scheduler_type

        s, stats = sched.run(metric,
                             apps,
                             app_data.video_desc,
                             sharing_type,
                             budget=budget)

    end = datetime.datetime.now()
    diff = end - start

    row = get_eval(len(apps), s, stats, budget, diff.microseconds, metric_key=metric) 

    return row

def main():
    args = get_args()

    setup_generator = Setup.SetupGenerator()
    setups = setup_generator.deserialize_setups(args.setups_file + ".pickle")

    # Write out each schedule generated by scheduler
    subdir = os.path.join(args.outdir, "schedules");
    if not os.path.exists(subdir):
        os.makedirs(subdir)

    if args.simulator:
        run_mode = "sim."
    else:
        run_mode = ""

    if args.scheduler_type == "greedy":
        outfile  = os.path.join(subdir, "greedy." + run_mode + args.run_id)
    elif args.scheduler_type == "hifi":
        outfile = os.path.join(subdir, "hifi." + run_mode + args.run_id)
    elif args.scheduler_type == "nosharing":
        outfile = os.path.join(subdir, "nosharing." + run_mode + args.run_id)
    elif args.scheduler_type == "maxsharing":
        outfile = os.path.join(subdir, "maxsharing." + run_mode + args.run_id)
    else:
        print args.scheduler_type, "must be in {greedy, hifi, nosharing, maxsharing}"
        sys.exit()

    f = open(outfile, 'w+')

    for setup in setups:

      # Get schedules generated by scheduler
      writer = csv.writer(f)

      row = run_scheduler(args.metric,
                          setup,
                          setup.uuid,
                          args.scheduler_type,
                          args.simulator)

      writer.writerow(row)
      f.flush()

    f.close()

if __name__ == "__main__":
    main()
