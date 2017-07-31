import sys
sys.path.append('src/scheduler')
import scheduler
import pprint as pp
import numpy as np
import time
import zmq

def flip(acc_map, total_layers):
    new_acc_map = {}
    for layer, acc in acc_map.iteritems():
        key = total_layers - layer
        new_acc_map[key] = acc
    return new_acc_map

# TODO: Get values from redis
accuracy_flowers_inception = {0:0.882,
                              4:0.882,
                              7:0.8834,
                              10:0.882,
                              11:0.8807,
                              14:0.8834,
                              17:0.8807,
                              18:0.882,
                              41:0.8807,
                              64:0.8807,
                              87:0.8807,
                              101:0.8765,
                              133:0.8779,
                              165:0.8765,
                              197:0.8697,
                              229:0.8615,
                              249:0.8669,
                              280:0.8477,
                              311:0.7284}

accuracy_trains_inception = flip({314:0.9855,
                            310:0.9855,
                            307:0.9831,
                            304:0.9879,
                            303:0.9879,
                            300:0.9879,
                            297:0.9831,
                            296:0.9831,
                            273:0.9831,
                            250:0.9831,
                            227:0.9831,
                            213:0.9831,
                            181:0.9831,
                            149:0.9855,
                            117:0.9952,
                            85:0.9952,
                            65:0.9952,
                            34:0.9831,
                            3:0.9080
                            #1:0.6610
                            }, 314)

accuracy_paris_inception = flip({314:0.8533,
                            310:0.8593,
                            307:0.8533,
                            304:0.8533,
                            303:0.8533,
                            300:0.8503,
                            297:0.8533,
                            296:0.8533,
                            273:0.8503,
                            250:0.8593,
                            227:0.8353,
                            213:0.8263,
                            181:0.8383,
                            149:0.8353,
                            117:0.8263,
                            85:0.8204,
                            65:0.8713,
                            34:0.8533,
                            3:0.7246
                            #1:0.2395
                            }, 314)

app_options = [{"accuracies": accuracy_flowers_inception,
                "model_path": "/home/ahjiang/models/flowers-40-0.0001-310-frozen.pb"},
               {"accuracies": accuracy_trains_inception,
                "model_path": "/home/ahjiang/models/trains-40-0.0001-310-frozen.pb"},
               {"accuracies": accuracy_paris_inception,
                "model_path": "/home/ahjiang/models/paris-95-frozen.pb"}]

model_desc = {"total_layers": 314,
              "channels": 1,
              "height": 299,
              "width": 299,
              "frozen_layer_names": {1: "input_1",
                                     4: "conv2d_1/convolution",
                                     7: "conv2d_2/convolution",
                                     10: "conv2d_3/convolution",
                                     11: "max_pooling2d_1/MaxPool",
                                     14: "conv2d_4/convolution",
                                     17: "conv2d_5/convolution",
                                     18: "max_pooling2d_2/MaxPool",
                                     41: "mixed0/concat",
                                     64: "mixed1/concat",
                                     87: "mixed2/concat",
                                     101: "mixed3/concat",
                                     133: "mixed4/concat",
                                     165: "mixed5/concat",
                                     197: "mixed6/concat",
                                     229: "mixed7/concat",
                                     249: "mixed8/concat",
                                     280: "mixed9/concat",
                                     311: "mixed10/concat",
                                     314: "dense_2/Softmax:0"}}

if __name__ == "__main__":

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    num_apps_range = int(sys.argv[1])
    outfile = sys.argv[2]
    thresholds = [0, 0.1, 0.05, 0.01, 0.005, 1]

    with open(outfile, "a+", 0) as f:
        for num_apps in range(1, num_apps_range + 1):
            for threshold in thresholds:

                # Get Schedule
                apps = []
                for i in range(1, num_apps + 1):
                    index = i % len(app_options)
                    app = app_options[index]
                    apps.append(app)
                if threshold == 0:
                    sched = scheduler.schedule_no_sharing(apps, model_desc)
                    print "------------", num_apps, "-----------"
                    pp.pprint(sched)
                else:
                    sched = scheduler.schedule(apps, threshold, model_desc)

                # Deploy schedule
                fpses = []
                for i in range(5):
                    socket.send_json(sched)
                    fps_message = socket.recv()
                    fpses.append(float(fps_message))
                avg_fps = np.average(fpses)
                stdev = np.std(fpses)
                line = str(num_apps) + "," + str(threshold) + "," + \
                       str(avg_fps) + "," + str(stdev) + "\n"
                f.write(line)
                print num_apps, threshold, avg_fps, stdev
