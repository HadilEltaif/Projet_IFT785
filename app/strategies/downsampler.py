from .preprocessing_strategy import PreprocessingStrategy

class DownsamplerStrategy(PreprocessingStrategy):
    def __init__(self, voxel_size=0.03):
        self.voxel_size = voxel_size

    def apply(self, pcd):
        return pcd.voxel_down_sample(self.voxel_size)
