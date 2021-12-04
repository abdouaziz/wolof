import torch
import numpy as np


def seed_all(seed_value):

    np.random.seed(seed_value)
    torch.manual_seed(seed_value)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed_value)
        torch.cuda.manual_seed_all(seed_value)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False


class WolofConfig:
    """
    Wolof configuraiton 
    """

    def __init__(self, config={}, *args, **kwargs):
        self.__config = config

    @property
    def Config(self):
        return self.__config

    @Config.setter
    def Config(self, config):
        self.__config = config

    def __getitem__(self, key):
        return self.__config[key]

    def __setitem__(self, key, value):
        self.__config[key] = value

    def load(self):
        """
        Load configuration from file
        """

        if not self.__config:
            self.__config = {
                "model_name": "bert-base-uncased",
                "max_len": 512,
                "batch_size": 32,
                "valid_batch_size": 32,
                "epochs": 5,
                "lr": 1e-5,
                "eps": 1e-8,
            }

        return self.__config
