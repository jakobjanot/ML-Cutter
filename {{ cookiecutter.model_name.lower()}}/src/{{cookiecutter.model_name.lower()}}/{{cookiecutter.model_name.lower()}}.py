from .config import hyperparams_dict
from .data import get_raw_data
from .features import build_features
from .model import train_model, predict
from .performance import measure_performance

class {{cookiecutter.model_name.capitalize()}}:
    def __init__(self):
        pass

    def get_raw_data(self):
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
