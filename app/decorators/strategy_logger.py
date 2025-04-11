import time

class StrategyLoggerDecorator:
    def __init__(self, strategy):
        self.strategy = strategy

    def apply(self, pcd):
        print(f"[LOG] Début de : {self.strategy.__class__.__name__}")
        start_time = time.time()

        result = self.strategy.apply(pcd)

        duration = time.time() - start_time
        print(f"[LOG] Fin de : {self.strategy.__class__.__name__} ({duration:.3f}s)")
        return result
