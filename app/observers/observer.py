class Observer:
    def update(self, event: str):
        raise NotImplementedError("Observer must implement the update() method")


class LoggerObserver(Observer):
    def update(self, event: str):
        print(f"[LoggerObserver] 📢 Événement reçu : {event}")


class PreprocessingNotifier:
    def __init__(self):
        self.observers = []

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def notify(self, event: str):
        for observer in self.observers:
            observer.update(event)
