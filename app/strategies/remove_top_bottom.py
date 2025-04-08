import numpy as np
from .preprocessing_strategy import PreprocessingStrategy

class RemoveTopBottomStrategy(PreprocessingStrategy):
    def __init__(self, z_min=-0.1, z_max=2.0):
        self.z_min = z_min
        self.z_max = z_max

    def apply(self, pcd):
        points = np.asarray(pcd.points)
        mask = (points[:, 2] >= self.z_min) & (points[:, 2] <= self.z_max)
        return pcd.select_by_index(np.where(mask)[0])
