from app.interfaces.loader_interface import ILoader
import numpy as np

class BINLoader(ILoader):
    def load(self, filepath):
        return np.fromfile(filepath, dtype=np.float32).reshape(-1, 4)
