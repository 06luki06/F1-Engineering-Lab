from abc import ABC, abstractmethod
import copy

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class EngineConfiguration():
    def __init__(self, mode: str, torque_map: list[int]):
        self.mode = mode
        self.torque_map = torque_map

class CarSetup(Prototype):
    def __init__(self, front_wing_angle: int, tyre_pressure_psi: float, engine: EngineConfiguration):
        self.front_wing_angle = front_wing_angle
        self.tyre_pressure_psi = tyre_pressure_psi
        self.engine = engine
    
    def clone(self):
        return copy.deepcopy(self)