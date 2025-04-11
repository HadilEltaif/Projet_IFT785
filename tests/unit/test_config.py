from app.utils.config import GlobalConfig

def test_global_config_singleton():
    c1 = GlobalConfig()
    c2 = GlobalConfig()
    assert c1 is c2  # Singleton vérifié

def test_config_modification():
    config = GlobalConfig()
    config.debug = True
    assert GlobalConfig().debug is True  # Même instance
