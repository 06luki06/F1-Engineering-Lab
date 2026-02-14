from abc import ABC
import pytest
from car_setup import CarSetup, EngineConfiguration, Prototype

def test_cloning_creates_new_object_reference():
    """
    TEST 1: Identity Check
    The clone must be a new object in memory, not just a reference to the old one.
    """
    engine = EngineConfiguration(mode="Race", torque_map=[100, 200, 300])
    original_setup = CarSetup(front_wing_angle=4, tyre_pressure_psi=21.0, engine=engine)
    
    cloned_setup = original_setup.clone()
    
    # Check that they are not the same object (is check)
    assert original_setup is not cloned_setup
    
    # Check that data was actually copied
    assert original_setup.front_wing_angle == cloned_setup.front_wing_angle
    assert original_setup.tyre_pressure_psi == cloned_setup.tyre_pressure_psi

def test_deep_copy_independence():
    """
    TEST 2: Deep Copy Verification (The Critical Test)
    Modifying the nested EngineConfiguration in the clone must NOT
    affect the original setup.
    """
    # 1. Setup Original (Hamilton's Car)
    engine_ham = EngineConfiguration(mode="Qualifying", torque_map=[500, 600])
    setup_hamilton = CarSetup(front_wing_angle=6, tyre_pressure_psi=22.5, engine=engine_ham)
    
    # 2. Clone for Teammate (Russell's Car)
    setup_russell = setup_hamilton.clone()
    
    # 3. Modify Russell's Engine
    setup_russell.engine.mode = "Save"
    setup_russell.engine.torque_map[0] = 100 # Detune the engine
    
    # 4. Assert Hamilton's car is untouched
    assert setup_hamilton.engine.mode == "Qualifying", "Original engine mode was altered! Deep copy failed."
    assert setup_hamilton.engine.torque_map[0] == 500, "Original torque map was altered! Deep copy failed."
    
    # 5. Assert Russell's car is changed
    assert setup_russell.engine.mode == "Save"

def test_independent_primitive_modification():
    """
    TEST 3: Primitive Value Independence
    Changing simple integers/floats on the clone shouldn't affect original.
    """
    engine = EngineConfiguration(mode="Race", torque_map=[1,2])
    setup_a = CarSetup(front_wing_angle=5, tyre_pressure_psi=20.0, engine=engine)
    setup_b = setup_a.clone()
    
    setup_b.front_wing_angle = 10
    
    assert setup_a.front_wing_angle == 5
    assert setup_b.front_wing_angle == 10

def test_interface_enforcement():
    """
    TEST 4: Interface Enforcement
    Ensure that the CarSetup class implements the clone method as required by the Prototype interface.
    """
    assert issubclass(Prototype, ABC), "Prototype class must inherit from abc.ABC!"

    with pytest.raises(TypeError):
        _ = Prototype()

    assert getattr(Prototype.clone, '__isabstractmethod__', False), "The 'clone' method must be decorated with @abstractmethod!"
