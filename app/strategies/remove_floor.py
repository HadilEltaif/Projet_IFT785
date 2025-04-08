import open3d as o3d
from .preprocessing_strategy import PreprocessingStrategy

class RemoveFloorStrategy(PreprocessingStrategy):
    def __init__(self, distance_threshold=0.05):
        self.distance_threshold = distance_threshold

    def apply(self, pcd):
        _, inliers = pcd.segment_plane(distance_threshold=self.distance_threshold,
                                       ransac_n=3,
                                       num_iterations=1000)
        return pcd.select_by_index(inliers, invert=True)
