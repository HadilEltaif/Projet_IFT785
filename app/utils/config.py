# app/utils/config.py

class GlobalConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GlobalConfig, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        # Paramètres globaux
        self.debug = False
        self.data_path = "data/"
        self.default_eps = 0.3
        self.default_min_samples = 5
        self.visualizer = "open3d"
        self.save_output = True
        self._initialized = True

    def __str__(self):
        return f"<GlobalConfig debug={self.debug}, eps={self.default_eps}, visualizer={self.visualizer}>"
