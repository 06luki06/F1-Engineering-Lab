import pytest
from abc import ABC
from power_unit_factory import (
    TeamFactory, FerrariFactory, MercedesFactory,
    ICE, ERS,
    FerrariICE, FerrariERS,
    MercedesICE, MercedesERS
)

def test_interfaces_are_abstract():
    """
    TEST 0: Pythonic Interface Enforcement
    Ensures that ICE, ERS, and TeamFactory are valid Abstract Base Classes.
    """
    # Check inheritance from ABC
    assert issubclass(TeamFactory, ABC)
    assert issubclass(ICE, ABC)
    assert issubclass(ERS, ABC)

    # Check that they cannot be instantiated
    with pytest.raises(TypeError):
        _ = TeamFactory()
    with pytest.raises(TypeError):
        _ = ICE()
    with pytest.raises(TypeError):
        _ = ERS()

def test_ferrari_family_integrity():
    """
    TEST 1: Ferrari Family Consistency
    The FerrariFactory must ONLY produce Ferrari components.
    """
    factory = FerrariFactory()
    
    ice = factory.create_ice()
    ers = factory.create_ers()
    
    # Check Types
    assert isinstance(ice, FerrariICE)
    assert isinstance(ers, FerrariERS)
    
    # Check Behavior
    assert "Ferrari" in ice.start()
    assert "heat" in ers.recover_energy() # Ferrari is known for heat recovery ;)

def test_mercedes_family_integrity():
    """
    TEST 2: Mercedes Family Consistency
    The MercedesFactory must ONLY produce Mercedes components.
    """
    factory = MercedesFactory()
    
    ice = factory.create_ice()
    ers = factory.create_ers()
    
    # Check Types
    assert isinstance(ice, MercedesICE)
    assert isinstance(ers, MercedesERS)
    
    # Check Behavior
    assert "Mercedes" in ice.start()
    assert "kinetic" in ers.recover_energy()

def test_client_decoupling():
    """
    TEST 3: Client Interface Usage
    This simulates the 'Client'. It shouldn't care which factory it has,
    as long as the parts work.
    """
    
    def assemble_f1_car(factory: TeamFactory):
        """Helper function simulating the Client (The Chassis)"""
        engine = factory.create_ice()
        battery = factory.create_ers()
        
        # Verify we got valid parts without knowing the brand
        assert isinstance(engine, ICE)
        assert isinstance(battery, ERS)
        return engine.start(), battery.recover_energy()

    # Test with Ferrari
    eng_sound, batt_status = assemble_f1_car(FerrariFactory())
    assert "Ferrari" in eng_sound
    assert "heat" in batt_status
    
    # Test with Mercedes
    eng_sound, batt_status = assemble_f1_car(MercedesFactory())
    assert "Mercedes" in eng_sound
    assert "kinetic" in batt_status