class PreprocessingStrategy:
    def apply(self, pcd):
        raise NotImplementedError("La méthode 'apply' doit être implémentée par les sous-classes.")


class PreprocessingPipeline:
    def __init__(self, strategies):
        self.strategies = strategies

    def run(self, pcd):
        for strategy in self.strategies:
            pcd = strategy.apply(pcd)
        return pcd
