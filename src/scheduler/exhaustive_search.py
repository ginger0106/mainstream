

import argparse
import csv
import fnmatch
import scheduler_util
import os
import sys
import app_data_mobilenets as app_data

sys.path.append('src/scheduler')
import run_scheduler_simulator as sim

sys.path.append('src/scheduler/types')
import Scheduler
import Setup

# TODO subdir everything into run_id?

# Directory structure
# outdir/
#   pointers.run_id.v0
#   setups.run_id.v0
#   setups.run_id.v0.pickle
#   setup/
#       configuration.setup_suffix.v0
#       model.setup_suffix.v0
#       environment.setup_suffix.v0
#   schedules/
#       greedy.run_id.v0
#       exhaustive.run_id.v0

def get_args(simulator=True):
    parser = argparse.ArgumentParser()
    app_names = [app["name"] for app in app_data.app_options]
    parser.add_argument("-n", "--num_apps_range", required=True, type=int)
    parser.add_argument("-o", "--outdir", required=True)
    parser.add_argument("-r", "--run_id", required=True)
    parser.add_argument("-v", "--verbose", type=int, default=0)
    parser.add_argument("-m", "--metric", default="f1")
    parser.add_argument("-s", "--setups_file")
    return parser.parse_args()


def get_eval(entry_id, s, stats, budget):
    row = [
        entry_id,
        stats["metric"],
    ]
    row += stats["frozen"]
    row += stats["fps"]
    row += [budget]
    return row


def write_cost_benefits_file(cost_benefits, outdir, filename):
    subdir = os.path.join(outdir, "setup");
    if not os.path.exists(subdir):
        os.makedirs(subdir)

    outfile = os.path.join(subdir, "configuration." + filename)
    with open(outfile, "w+") as f:
        for app_id, d1 in cost_benefits.iteritems():
            for num_frozen, d2 in d1.iteritems():
                for target_fps, d3 in d2.iteritems():
                    cost = d3[0]
                    benefit = d3[1]
                    line = "{} {} {} {} {}\n".format(app_id,
                                                     num_frozen,
                                                     target_fps,
                                                     cost,
                                                     benefit)
                    f.write(line)
    return outfile


def write_model_file(layer_costs, outdir, filename):
    subdir = os.path.join(outdir, "setup");
    if not os.path.exists(subdir):
        os.makedirs(subdir)

    outfile = os.path.join(subdir, "model." + filename)
    with open(outfile, "w+") as f:
        layer_costs_str = [str(c) for c in layer_costs]
        line = " ".join(layer_costs_str) + "\n"
        f.write(line)
    return outfile


def write_environment_file(budget, outdir, filename):
    subdir = os.path.join(outdir, "setup");
    if not os.path.exists(subdir):
        os.makedirs(subdir)

    outfile = os.path.join(subdir, "environment." + filename)
    with open(outfile, "w+") as f:
        line = str(budget) + "\n"
        f.write(line)
    return outfile

def write_intermediate_files(args, setup, setup_suffix):

    apps = [app.to_map() for app in setup.apps]
    budget = setup.budget

    s = Scheduler.Scheduler(args.metric,
                            apps,
                            setup.video_desc.to_map(),
                            app_data.model_desc,
                            0)

    # Write cost benefits, model, and environment data for cpp fn
    cost_benefits = s.get_cost_benefits()
    f1 = write_cost_benefits_file(cost_benefits, args.outdir, setup_suffix)
    f2 = write_model_file(s.model.layer_latencies, args.outdir, setup_suffix)
    f3 = write_environment_file(budget, args.outdir, setup_suffix)

    # Get output with mainstream-simulator schedules
    s, stats = sim.run_simulator(args.metric, apps, budget)
    row = get_eval(len(apps), s, stats, budget)

    return row


def run_scheduler(args, setup, setup_suffix):

    apps = [app.to_map() for app in setup.apps]
    budget = setup.budget

    s = Scheduler.Scheduler(args.metric,
                            apps,
                            setup.video_desc.to_map(),
                            app_data.model_desc,
                            0)

    # Write cost benefits, model, and environment data for cpp fn
    cost_benefits = s.get_cost_benefits()
    f1 = write_cost_benefits_file(cost_benefits, args.outdir, setup_suffix)
    f2 = write_model_file(s.model.layer_latencies, args.outdir, setup_suffix)
    f3 = write_environment_file(budget, args.outdir, setup_suffix)

    # Get output with mainstream-simulator schedules
    s, stats = sim.run_simulator(args.metric, apps, budget)
    row = get_eval(len(apps), s, stats, budget)

    return row


def main():
    args = get_args()

    setup_generator = Setup.SetupGenerator()
    setups = setup_generator.deserialize_setups(args.setups_file + ".pickle")

    rows = []
    pointers_file = os.path.join(args.outdir, "pointers." + args.run_id)
    with open(pointers_file, "w+") as f:
        for setup in setups:

          # Write out filenames which point to schedule data
          setup_suffix = setup.uuid
          line = "{}\n".format(setup_suffix)
          f.write(line)
          f.flush()

          # Get schedules generated by scheduler
          row = run_scheduler(args, setup, setup_suffix)
          rows.append(row)

          # Write out intermediate files
          write_intermediate_files(args, setup, setup_suffix)


    # Write out each schedule generated by scheduler
    subdir = os.path.join(args.outdir, "schedules");
    if not os.path.exists(subdir):
        os.makedirs(subdir)
    schedules_file = os.path.join(subdir, "greedy." + args.run_id)
    with open(schedules_file, "w+") as f:
        for row in rows:
            writer = csv.writer(f)
            writer.writerow(row)
            f.flush()


if __name__ == "__main__":
    main()
