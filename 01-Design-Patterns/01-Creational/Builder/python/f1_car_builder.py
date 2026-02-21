from dataclasses import dataclass
from typing import Optional
from abc import ABC, abstractmethod

@dataclass
class F1Car:
    chassis: Optional[str] = None
    engine: Optional[str] = None
    front_wing: Optional[str] = None
    rear_wing: Optional[str] = None
    tires: Optional[str] = None

    def show_specs(self):
        specs = (f"--- F1 Car Configuration ---\n"
                 f"Chassis:    {self.chassis}\n"
                 f"Engine:     {self.engine}\n"
                 f"Front Wing: {self.front_wing}\n"
                 f"Rear Wing:  {self.rear_wing}\n"
                 f"Tires:      {self.tires}\n"
                 f"---------------------------")
        print(specs)

class CarBuilder(ABC):
    def reset(self) -> None:
        self._car = F1Car()
    
    @abstractmethod
    def build_chassis(self) -> None:
        pass

    def build_engine(self) -> None:
        self._car.engine = "V6 Turbo" 

    @abstractmethod
    def build_wings(self) -> None:
        pass

    @abstractmethod
    def build_tires(self) -> None:
        pass

    def get_result(self) -> F1Car:
        product = self._car
        self.reset()
        return product

class MonacoBuilder(CarBuilder):
    def __init__(self):
        self.reset()

    def build_chassis(self) -> None:
        self._car.chassis = "Monaco Carbon Monocoque"

    def build_wings(self) -> None:
        self._car.front_wing = "High Downforce Front Wing"
        self._car.rear_wing = "High Downforce Rear Wing"

    def build_tires(self) -> None:
        self._car.tires = "Soft Tires"
    
class MonzaBuilder(CarBuilder):
    def __init__(self):
        self.reset()

    def build_chassis(self) -> None:
        self._car.chassis = "Monza Carbon Monocoque"

    def build_wings(self) -> None:
        self._car.front_wing = "Low Drag Front Wing"
        self._car.rear_wing = "Low Drag Rear Wing"

    def build_tires(self) -> None:
        self._car.tires = "Hard Tires"

class RaceEngineer:
    def construct_car(self, builder: CarBuilder) -> None:
        builder.reset()
        builder.build_chassis()
        builder.build_engine()
        builder.build_wings()
        builder.build_tires()