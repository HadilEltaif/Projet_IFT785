
import numpy as np
from app.clustering.adaptive_clustering import AdaptiveClustering

class ClusteringService:
    @staticmethod
    def cluster_points(points):
        clustering_algo = AdaptiveClustering()
        clusters = clustering_algo.adaptive_clustering(points)
        return clusters
