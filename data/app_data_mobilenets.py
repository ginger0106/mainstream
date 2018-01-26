

accuracy_flowers_mobilenets = {45:0.8258,
                              51:0.8258,
                              57:0.8203,
                              63:0.8107,
                              69:0.7860,
                              75:0.7092,
                              81:0.1468}

prob_fpr_flowers_mobilenets = {45:0.8258,
                              51:0.8258,
                              57:0.8203,
                              63:0.8107,
                              69:0.7860,
                              75:0.7092,
                              81:0.1468}


app_options = [{"accuracies": accuracy_flowers_mobilenets,
                "prob_fprs" : prob_fpr_flowers_mobilenets,
                "event_length_ms": 2500,
                "correlation": 0.1664,
                "model_path": {3:"flowers-mobilenet-80-frozen.pb",
                               9:"flowers-mobilenet-80-frozen.pb",
                               15:"flowers-mobilenet-80-frozen.pb",
                               21:"flowers-mobilenet-80-frozen.pb",
                               27:"flowers-mobilenet-80-frozen.pb",
                               33:"flowers-mobilenet-80-frozen.pb",
                               39:"flowers-mobilenet-80-frozen.pb",
                               45:"flowers-mobilenet-80-frozen.pb",
                               51:"flowers-mobilenet-80-frozen.pb",
                               57:"flowers-mobilenet-80-frozen.pb",
                               63:"flowers-mobilenet-80-frozen.pb",
                               69:"flowers-mobilenet-80-frozen.pb",
                               75:"flowers-mobilenet-80-frozen.pb",
                               81:"flowers-mobilenet-80-frozen.pb",
                               84:"flowers-mobilenet-80-frozen.pb"}}]

mobilenets_layer_latencies = [1.0, 1.0, 1.0, 0.8685, 0.8685, 0.8685, 0.8685,
        0.8685, 0.8685, 0.4863, 0.4863, 0.4863, 0.4863, 0.4863, 0.4863, 0.6383,
        0.6383, 0.6383, 0.6383, 0.6383, 0.6383, 0.3557, 0.3557, 0.3557, 0.3557,
        0.3557, 0.3557, 0.2155, 0.2155, 0.2155, 0.2155, 0.2155, 0.2155, 0.0248,
        0.0248, 0.0248, 0.0248, 0.0248, 0.0248, 0.0378, 0.0378, 0.0378, 0.0378,
        0.0378, 0.0378, 0.0373, 0.0373, 0.0373, 0.0373, 0.0373, 0.0373, 0.0594,
        0.0594, 0.0594, 0.0594, 0.0594, 0.0594, 0.0497, 0.0497, 0.0497, 0.0497,
        0.0497, 0.0497, 0.0428, 0.0428, 0.0428, 0.0428, 0.0428, 0.0428, 0.0626,
        0.0626, 0.0626, 0.0626, 0.0626, 0.0626, 0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.0109, 0.0109, 0.0109]

model_desc = {"total_layers": 84,
              "channels": 1,
              "height": 299,
              "width": 299,
              "layer_latencies": mobilenets_layer_latencies,
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

video_desc = {"stream_fps": 14}

