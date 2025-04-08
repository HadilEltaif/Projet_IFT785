import numpy as np
from .preprocessing_strategy import PreprocessingStrategy

class RemoveSidePointsStrategy(PreprocessingStrategy):
    def __init__(self, x_min=-0.5, x_max=0.5):
        self.x_min = x_min
        self.x_max = x_max

    def apply(self, pcd):
        points = np.asarray(pcd.points)
        mask = (points[:, 0] >= self.x_min) & (points[:, 0] <= self.x_max)
        return pcd.select_by_index(np.where(mask)[0])
