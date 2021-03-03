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
        return 

    def build_features(self):
        return 

    def train_model(self):
        return 

    def measure_performance(self):
        return 

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
        return

    def download_network(self):
        return 

    def load_network(self):
        return 
