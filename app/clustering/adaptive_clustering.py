
import numpy as np
from sklearn.cluster import DBSCAN

class AdaptiveClustering:
    def __init__(self, cluster_size_min=3, cluster_size_max=2200000):
        self.cluster_size_min = cluster_size_min
        self.cluster_size_max = cluster_size_max
        self.region_max = 10
        self.regions = [2, 3, 3, 3, 3, 3, 3, 2, 3, 3]

    def divide_to_regions(self, points):
        regions = [[] for _ in range(self.region_max)]
        ranges = np.cumsum([0] + self.regions)
        distances = np.linalg.norm(points[:, :2], axis=1)
        for i in range(self.region_max):
            mask = (distances > ranges[i]) & (distances <= ranges[i+1])
            regions[i] = points[mask]
        return regions

    def adaptive_clustering(self, points):
        regions = self.divide_to_regions(points)
        clusters = []
        for i, region in enumerate(regions):
            if len(region) < self.cluster_size_min:
                continue
            eps = 0.08 * (i + 1)
            dbscan = DBSCAN(eps=eps, min_samples=self.cluster_size_min)
            labels = dbscan.fit_predict(region)
            for label in set(labels):
                if label == -1:
                    continue
                cluster = region[labels == label]
                if self.cluster_size_min <= len(cluster) <= self.cluster_size_max:
                    clusters.append(cluster)
        return clusters
