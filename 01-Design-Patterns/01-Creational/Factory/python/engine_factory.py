from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self) -> str:
        pass

    @abstractmethod
    def stop(self) -> str:
        pass

    @abstractmethod
    def get_spec(self) -> str:
        pass

class FerrariEngine(Engine):
    def start(self) -> str:
        return "Bwoah! V6 sounds"
    
    def stop(self) -> str:
        return "Ferrari engine stopped."
    
    def get_spec(self) -> str:
        return "Ferrari Engine: 3.0L V6, 620 HP"
    
class MercedesEngine(Engine):
    def start(self) -> str:
        return "Hummm! V6 sounds"
    
    def stop(self) -> str:
        return "Mercedes engine stopped."
    
    def get_spec(self) -> str:
        return "Mercedes Engine: 4.0L V6, 603 HP"
    
class EngineFactory:
    _engines = {
        "Ferrari": FerrariEngine,
        "Mercedes": MercedesEngine
    }

    def get_engine(self, manufacturer: str) -> Engine:
        engine_cls = self._engines.get(manufacturer)
        if not engine_cls:
            raise ValueError(f"Unknown manufacturer: {manufacturer}")
        return engine_cls()