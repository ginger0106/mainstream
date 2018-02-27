import sys

pedestrian_correlation_coefficient = .107 # Derived from pedestrian dataset, get_cp_ratio
train_correlation_coefficient = .125 # Derived from train dataset, get_cp_ratio
correlation_coefficient = .107 # Derived from pedestrian dataset, get_cp_ratio

def get_cp(acc, correlation_coefficient):
    delta_opt = acc
    cp = (1 - acc) + delta_opt * correlation_coefficient
    return cp

model_paths = {0:  "flowers-310-frozen.pb",
               4:  "flowers-310-frozen.pb",
               7:  "flowers-310-frozen.pb",
               10: "flowers-310-frozen.pb",
               11: "flowers-310-frozen.pb",
               14: "flowers-310-frozen.pb",
               17: "flowers-310-frozen.pb",
               18: "flowers-310-frozen.pb",
               41: "flowers-310-frozen.pb",
               64: "flowers-310-frozen.pb",
               87: "flowers-310-frozen.pb",
               101:"flowers-310-frozen.pb",
               133:"flowers-310-frozen.pb",
               165:"flowers-310-frozen.pb",
               197:"flowers-310-frozen.pb",
               229:"flowers-310-frozen.pb",
               249:"flowers-310-frozen.pb",
               280:"flowers-310-frozen.pb",
               311:"flowers-310-frozen.pb"}

################# SYNTHETIC ##################

accuracy_flowers_inception = {0:0.8820,
                              4:0.8807,
                              7:0.8834,
                              10:0.8820,
                              11:0.8807,
                              14:0.8807,
                              17:0.8807,
                              18:0.8820,
                              41:0.8793,
                              64:0.8807,
                              87:0.8807,
                              101:0.8765,
                              133:0.8779,
                              165:0.8765,
                              197:0.8697,
                              229:0.8669,
                              249:0.8477,
                              280:0.7284,
                              311:0.2606}

prob_tnr_flowers_inception = {0:0.0297,
                              4:0.0301,
                              7:0.0293,
                              10:0.0297,
                              11:0.0300,
                              14:0.0300,
                              17:0.0300,
                              18:0.0296,
                              41:0.0304,
                              64:0.0300,
                              87:0.0300,
                              101:0.0310,
                              133:0.0307,
                              165:0.0311,
                              197:0.0329,
                              229:0.0335,
                              249:0.0384,
                              280:0.0693,
                              311:0.1893}

accuracy_cars_inception = {0:0.8862,
                            4:0.8862,
                            7:0.8897,
                            10:0.8862,
                            11:0.8862,
                            14:0.8931,
                            17:0.8897,
                            18:0.8897,
                            41:0.8931,
                            64:0.8793,
                            87:0.8793,
                            101:0.8793,
                            133:0.8793,
                            165:0.8862,
                            197:0.8793,
                            229:0.8655,
                            249:0.8345,
                            280:0.6414,
                            311:0.2690}

prob_tnr_cars_inception = {0:0.0242,
                            4:0.0241,
                            7:0.0234,
                            10:0.0242,
                            11:0.0242,
                            14:0.0227,
                            17:0.0234,
                            18:0.0234,
                            41:0.0227,
                            64:0.0255,
                            87:0.0256,
                            101:0.0257,
                            133:0.0256,
                            165:0.0241,
                            197:0.0255,
                            229:0.0284,
                            249:0.0349,
                            280:0.0763,
                            311:0.1569}

accuracy_cats_inception = {}
prob_tnr_cats_inception = {}

################# REAL ##################

accuracy_pedestrian_inception = {0:0.8201,
                                 4:0.8201,
                                 7:0.8266,
                                 10:0.8360,
                                 11:0.8320,
                                 14:0.8315,
                                 17:0.8295,
                                 18:0.8285,
                                 41:0.8365,
                                 64:0.8370,
                                 87:0.8330,
                                 101:0.8434,
                                 133:0.8479,
                                 165:0.8533,
                                 197:0.8588,
                                 229:0.8632,
                                 249:0.8855,
                                 280:0.8999,
                                 311:0.4504}

prob_tnr_pedestrian_inception ={0:0.1968,
                                4:0.1974,
                                7:0.1884,
                                10:0.1782,
                                11:0.1830,
                                14:0.1840,
                                17:0.1858,
                                18:0.1869,
                                41:0.1770,
                                64:0.1766,
                                87:0.1809,
                                101:0.1675,
                                133:0.1615,
                                165:0.1536,
                                197:0.1409,
                                229:0.1432,
                                249:0.1142,
                                280:0.0925,
                                311:0.5001}

pedestrian_app = {"accuracies": accuracy_pedestrian_inception,
                "prob_tnrs" : prob_tnr_pedestrian_inception,
                "event_length_ms": 500,
                "event_frequency": 0.3,
                "correlation_coefficient": pedestrian_correlation_coefficient,
                "model_path": model_paths,
                "name": "pedestrian"}

cars_app = {"accuracies": accuracy_cars_inception,
            "prob_tnrs" : prob_tnr_cars_inception,
            "event_length_ms": 500,
            "event_frequency": 0.5,
            "correlation_coefficient": correlation_coefficient,
            "model_path": model_paths,
            "name": "cars"}

cats_app = {"accuracies": accuracy_cats_inception,
            "prob_tnrs" : prob_tnr_cats_inception,
            "event_length_ms": 500,
            "event_frequency": 0.3,
            "correlation_coefficient": correlation_coefficient,
            "model_path": model_paths,
            "name": "cats"}

flowers_app = {"accuracies": accuracy_flowers_inception,
               "prob_tnrs" : prob_tnr_flowers_inception,
               "event_length_ms": 500,
               "event_frequency": 0.2,
               "correlation_coefficient": correlation_coefficient,
               "model_path": model_paths,
               "name": "flowers"}

app_options = [
               pedestrian_app,
               cars_app,
               flowers_app,
               cats_app,
               ]

apps_by_name = {app["name"]: app for app in app_options}


inception_layer_latencies =  [0.179, 0.179, 0.179, 0.179, 0.3691, 0.3691,
        0.3691, 0.4197, 0.4197, 0.4197, 1.0, 0.0313, 0.0313, 0.0313, 0.5492,
        0.5492, 0.5492, 0.6753, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542,
        0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542,
        0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0542, 0.0607,
        0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607,
        0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607, 0.0607,
        0.0607, 0.0607, 0.0607, 0.0607, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621,
        0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621,
        0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621, 0.0621,
        0.0853, 0.0853, 0.0853, 0.0853, 0.0853, 0.0853, 0.0853, 0.0853, 0.0853,
        0.0853, 0.0853, 0.0853, 0.0853, 0.0853, 0.0352, 0.0352, 0.0352, 0.0352,
        0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352,
        0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352,
        0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352, 0.0352,
        0.0352, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033,
        0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033,
        0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033,
        0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0033, 0.0052, 0.0052, 0.0052,
        0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052,
        0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052,
        0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052, 0.0052,
        0.0052, 0.0052, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087,
        0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087,
        0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087,
        0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0087, 0.0091, 0.0091,
        0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091,
        0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091, 0.0091,
        0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054,
        0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054,
        0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054, 0.0054,
        0.0054, 0.0054, 0.0054, 0.0054, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051,
        0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051,
        0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051,
        0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0051, 0.0509,
        0.0509, 0.0509]

model_desc = {"total_layers": 314,
              "channels": 1,
              "height": 299,
              "width": 299,
              "layer_latencies": inception_layer_latencies,
              "frozen_layer_names": {1:"input_1",
                          3:"conv1_relu/clip_by_value",
                          9:"conv_pw_1_relu/clip_by_value",
                          15:"conv_pw_2_relu/clip_by_value",
                          21:"conv_pw_3_relu/clip_by_value",
                          27:"conv_pw_4_relu/clip_by_value",
                          33:"conv_pw_5_relu/clip_by_value",
                          39:"conv_pw_6_relu/clip_by_value",
                          45:"conv_pw_7_relu/clip_by_value",
                          51:"conv_pw_8_relu/clip_by_value",
                          57:"conv_pw_9_relu/clip_by_value",
                          63:"conv_pw_10_relu/clip_by_value",
                          69:"conv_pw_11_relu/clip_by_value",
                          75:"conv_pw_12_relu/clip_by_value",
                          81:"conv_pw_13_relu/clip_by_value",
                          84:"dense_2/Softmax:0"}}

video_desc = {"stream_fps": 15}

