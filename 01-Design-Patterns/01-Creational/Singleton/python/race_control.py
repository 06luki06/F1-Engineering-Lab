import threading

class Singleton(type):
    _instances = {}
    _lock = threading.Lock()  # Ensures thread-safe singleton creation

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
    
class RaceControl(metaclass=Singleton):
    def __init__(self):
        self._race_status: str = "GREEN"
        self._lock = threading.Lock()

    @staticmethod
    def get_instance():
        return RaceControl()

    def get_status(self) -> str:
        with self._lock:
            return self._race_status
    
    def update_status(self, status: str) -> None:
        allowed_status = ["GREEN", "YELLOW", "RED", "SAFETY_CAR"]
        if status not in allowed_status:
            raise ValueError(f"Status must be one of {allowed_status}")
        with self._lock:
            self._race_status = status