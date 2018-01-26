

accuracy_flowers_inception = {7:0.8834,
                              18:0.8820,
                              87:0.8807,
                              133:0.8779,
                              165:0.8765,
                              197:0.8697,
                              229:0.8669,
                              249:0.8477,
                              280:0.7284,
                              311:0.2606}

prob_fpr_flowers_inception = {7:0.0293,
                              18:0.0296,
                              87:0.0300,
                              133:0.0307,
                              165:0.0311,
                              197:0.0329,
                              229:0.0335,
                              249:0.0384,
                              280:0.0693,
                              311:0.1893}

app_options = [{"accuracies": accuracy_flowers_inception,
                "prob_fprs" : prob_fpr_flowers_inception,
                "event_length_ms": 500,
                "correlation": 0.1664,
                "model_path": {
                    0:  "flowers-mobilenet-80-frozen.pb",
                    4:  "flowers-mobilenet-80-frozen.pb",
                    7:  "flowers-mobilenet-80-frozen.pb",
                    10: "flowers-mobilenet-80-frozen.pb",
                    11: "flowers-mobilenet-80-frozen.pb",
                    14: "flowers-mobilenet-80-frozen.pb",
                    17: "flowers-mobilenet-80-frozen.pb",
                    18: "flowers-mobilenet-80-frozen.pb",
                    41: "flowers-mobilenet-80-frozen.pb",
                    64: "flowers-mobilenet-80-frozen.pb",
                    87: "flowers-mobilenet-80-frozen.pb",
                    101:"flowers-mobilenet-80-frozen.pb",
                    133:"flowers-mobilenet-80-frozen.pb",
                    165:"flowers-mobilenet-80-frozen.pb",
                    197:"flowers-mobilenet-80-frozen.pb",
                    229:"flowers-mobilenet-80-frozen.pb",
                    249:"flowers-mobilenet-80-frozen.pb",
                    280:"flowers-mobilenet-80-frozen.pb",
                    311:"flowers-mobilenet-80-frozen.pb"}
                }
               ]

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
              "frozen_layer_names": {0:"input_1",
                          3:"conv1_relu",
                          9:"conv_pw_1_relu",
                          15:"conv_pw_2_relu",
                          21:"conv_pw_3_relu",
                          27:"conv_pw_4_relu",
                          33:"conv_pw_5_relu",
                          39:"conv_pw_6_relu",
                          45:"conv_pw_7_relu",
                          51:"conv_pw_8_relu",
                          57:"conv_pw_9_relu",
                          63:"conv_pw_10_relu",
                          69:"conv_pw_11_relu",
                          75:"conv_pw_12_relu",
                          81:"conv_pw_13_relu",
                          84:"dense_2"}}

video_desc = {"stream_fps": 14}

'''
# Layer latencies without 2 bug fixes. However, gives stable results.
inception_layer_latencies =  [0.0888, 0.0888, 0.0888, 0.0888, 0.1373, 0.1373,
        0.1373, 0.2449, 0.2449, 0.2449, 0.2613, 0.2565, 0.2565, 0.2565, 0.4655,
        0.4655, 0.4655, 0.3402, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201,
        0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201,
        0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.6201, 0.5133,
        0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133,
        0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133, 0.5133,
        0.5133, 0.5133, 0.5133, 0.5133, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973,
        0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973,
        0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973, 0.7973,
        0.6614, 0.6614, 0.6614, 0.6614, 0.6614, 0.6614, 0.6614, 0.6614, 0.6614,
        0.6614, 0.6614, 0.6614, 0.6614, 0.6614, 0.9368, 0.9368, 0.9368, 0.9368,
        0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368,
        0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368,
        0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368, 0.9368,
        0.9368, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744,
        0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744,
        0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744,
        0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.6744, 0.9576, 0.9576, 0.9576,
        0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576,
        0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576,
        0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576, 0.9576,
        0.9576, 0.9576, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091,
        0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091,
        0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091,
        0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.7091, 0.9803, 0.9803,
        0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803,
        0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803, 0.9803,
        0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298,
        0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298,
        0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298, 0.7298,
        0.7298, 0.7298, 0.7298, 0.7298, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
        1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0,
        1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.7424, 0.7424, 0.7242]
        '''
