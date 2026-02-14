from abc import ABC, abstractmethod

#region Abstract Classes
class ICE(ABC):
    @abstractmethod
    def start(self):
        pass

class ERS(ABC):
    @abstractmethod
    def recover_energy(self):
        pass

class TeamFactory(ABC):
    @abstractmethod
    def create_ice(self) -> ICE:
        pass

    @abstractmethod
    def create_ers(self) -> ERS:
        pass
#endregion

#region Concrete Implementations
class FerrariICE(ICE):
    def start(self):
        return "Ferrari ICE roaring to life!"
    
class FerrariERS(ERS):
    def recover_energy(self):
        return "Ferrari ERS recovering heat energy!"

class MercedesICE(ICE):
    def start(self):
        return "Mercedes ICE purring smoothly!"
    
class MercedesERS(ERS):
    def recover_energy(self):
        return "Mercedes ERS recovering kinetic energy!"
#endregion

#region Concrete Factories
class FerrariFactory(TeamFactory):
    def create_ice(self) -> ICE:
        return FerrariICE()
    
    def create_ers(self) -> ERS:
        return FerrariERS()
    
class MercedesFactory(TeamFactory):
    def create_ice(self) -> ICE:
        return MercedesICE()
    
    def create_ers(self) -> ERS:
        return MercedesERS()
#endregion