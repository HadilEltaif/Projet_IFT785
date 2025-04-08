from .preprocessing_strategy import PreprocessingStrategy

class RemoveOutliersStrategy(PreprocessingStrategy):
    def __init__(self, nb_neighbors=20, std_ratio=2.0):
        self.nb_neighbors = nb_neighbors
        self.std_ratio = std_ratio

    def apply(self, pcd):
        pcd, _ = pcd.remove_statistical_outlier(nb_neighbors=self.nb_neighbors,
                                                 std_ratio=self.std_ratio)
        return pcd
