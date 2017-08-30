
class NeuralNet:
    # Represents a Streamer NeuralNetEvaluator
    def __init__(self, net_id, model_obj, parent_id=None, start=None,
                       end=None, shared=None, model_path=None):
        self.net_id = net_id

        self.data = {"net_id": self.net_id,
                     "channels": model_obj.channels,
                     "width": model_obj.width,
                     "height": model_obj.height}

        if parent_id != None:
            self.parent_id = parent_id
            self.data["parent_id"] = parent_id
        if start != None:
            self.start = start
            self.data["input_layer"] = model_obj.frozen_layer_names[start]
        if end != None:
            self.end = end
            if end != 0:            # Starting condition
                self.data["output_layer"] = model_obj.frozen_layer_names[end]
        if shared != None:
            self.shared = shared
            self.data["shared"] = shared
        if model_path != None:
            self.model_path = model_path
            self.data["model_path"] = model_path

    def __str__(self):
        return self.data

class Model:
    def __init__(self, model_desc):
        self.channels = model_desc["channels"]
        self.height = model_desc["height"]
        self.width = model_desc["width"]
        self.final_layer = model_desc["total_layers"]
        self.frozen_layer_names = model_desc["frozen_layer_names"]

class Schedule:
    # Represents a Streamer schedule
    def __init__(self):
        self.next_id = 0
        self.schedule = []

    def add_neural_net(self, net):
        self.schedule.append(net.data)

    def get_id(self):
        next_id = self.next_id
        self.next_id += 1
        return next_id
