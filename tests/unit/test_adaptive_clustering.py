import numpy as np
from app.clustering.adaptive_clustering import AdaptiveClustering

def test_divide_to_regions():
    clustering = AdaptiveClustering()
    points = np.random.rand(100, 3) * 30
    regions = clustering.divide_to_regions(points)

    assert len(regions) == clustering.region_max

    total_points = sum(len(region) for region in regions)

    # Accepte un peu de perte (filtrage logique)
    assert total_points <= 100
    assert total_points >= 60  # au moins 60% des points doivent rester

def test_adaptive_clustering_returns_clusters():
    clustering = AdaptiveClustering()
    # Créer 3 petits clusters de points proches
    cluster_1 = np.random.normal(loc=[2, 2, 2], scale=0.01, size=(10, 3))
    cluster_2 = np.random.normal(loc=[8, 8, 8], scale=0.01, size=(10, 3))
    cluster_3 = np.random.normal(loc=[15, 15, 15], scale=0.01, size=(10, 3))
    points = np.vstack([cluster_1, cluster_2, cluster_3])

    clusters = clustering.adaptive_clustering(points)
    assert isinstance(clusters, list)
    assert len(clusters) >= 3
    for cluster in clusters:
        assert cluster.shape[1] == 3
        assert len(cluster) >= clustering.cluster_size_min
