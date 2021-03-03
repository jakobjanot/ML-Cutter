from .config import hyperparams_dict
from .data import get_model_data
from .features import build_features
from .model import Network, train_model, predict, download_network
from .performance import measure_performance

class {{cookiecutter.model_name.capitalize()}}:
    def __init__(self):

        self.network = Network()
        self.hyperparams = hyperparams_dict

    def get_model_data(self):
        return get_model_data()

    def build_features(self):
        return build_features()

    def train_model(self):
        return train_model()

    def measure_performance(self):
        return measure_performance()

    def build_model(self):

        # get model data
        self.get_model_data()

        # build features
        self.build_features()

        # train model
        self.train_model()

        # measure performance
        self.measure_performance()


    def predict(self):
        return predict()

    def download_network(self):
        return download_network()

    def load_network(self):
        return None
