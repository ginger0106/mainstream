import sys
sys.path.append('src/scheduler')
import Scheduler
sys.path.append('data')
import app_data
import pprint as pp
import time
import zmq

if __name__ == "__main__":

    num_apps_range = int(sys.argv[1])
    version = int(sys.argv[2])
    outfile_prefix = sys.argv[3]

    if version not in range(0, 3):
        print "Version should be 0 for mainstream, 1 for nosharing, 2 for maxsharing"
        sys.exit()

    outfile_nosharing = outfile_prefix + "-nosharing"
    outfile_maxsharing = outfile_prefix + "-maxsharing"
    outfile_mainstream = outfile_prefix + "-mainstream"

    params_nosharing = [True, False]
    params_maxsharing = [False, True]
    params_mainstream = [False, False]

    outfiles = [outfile_nosharing, outfile_maxsharing, outfile_mainstream]
    params_options = [params_nosharing, params_maxsharing, params_mainstream]

    outfile = outfiles[version]
    params = params_options[version]

    correlations = [0, .1664, 1]

    num_trials = 3

    for i in range(num_trials):
        for outfile, params in zip(outfiles, params_options):
            if outfile != outfile_mainstream:
                continue
            for c in correlations:
                outfile_full = outfile + "-c" + str(c)
                print outfile_full
                with open(outfile_full, "a+", 0) as f:
                    for num_apps in range(2, num_apps_range+1):

                        # Get Schedule
                        apps = []
                        for i in range(1, num_apps + 1):
                            index = i % len(app_data.app_options)
                            app = dict(app_data.app_options[index])
                            app["app_id"] = i
                            app["correlation"] = c
                            apps.append(app)

                        s = Scheduler.Scheduler(apps, app_data.video_desc,
                                                app_data.model_desc, 0)

                        metric, cost, avg_rel_acc, num_frozen_list, target_fps_list = s.run(150,
                                                                                      params[0],
                                                                                      params[1])
                        print "Observed FNR:", metric, ", Frozen:", num_frozen_list, \
                                ", FPS:",  target_fps_list, ", Cost:", cost

                        num_frozen_str = ",".join([str(x) for x in num_frozen_list])
                        target_fps_str = ",".join([str(x) for x in target_fps_list])

                        line = str(num_apps) + "," + str(round(metric, 4)) + "," + \
                               str(round(avg_rel_acc ,4)) + "," + \
                               num_frozen_str + "," + target_fps_str + "\n"
                        f.write(line)
