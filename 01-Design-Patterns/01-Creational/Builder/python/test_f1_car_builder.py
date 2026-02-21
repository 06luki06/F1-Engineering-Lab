import pytest
from abc import ABC
from f1_car_builder import (
    F1Car, CarBuilder, 
    MonacoBuilder, MonzaBuilder, 
    RaceEngineer
)

def test_builder_interface_is_abstract():
    """
    TEST 0: Interface Enforcement
    Ensures that CarBuilder is a valid Abstract Base Class and cannot be instantiated.
    """
    assert issubclass(CarBuilder, ABC)
    
    with pytest.raises(TypeError):
        # Should fail because abstract methods are not implemented
        _ = CarBuilder()

def test_monaco_high_downforce_setup():
    """
    TEST 1: Monaco Configuration
    The MonacoBuilder must produce a car optimized for tight corners.
    """
    builder = MonacoBuilder()
    engineer = RaceEngineer()
    
    # Director coordinates the build
    engineer.construct_car(builder)
    car = builder.get_result()
    
    assert isinstance(car, F1Car)
    assert "High Downforce" in car.front_wing
    assert "High Downforce" in car.rear_wing
    assert "Soft" in car.tires
    assert "Monaco" in car.chassis

def test_monza_low_drag_setup():
    """
    TEST 2: Monza Configuration
    The MonzaBuilder must produce a car optimized for top speed (Temple of Speed).
    """
    builder = MonzaBuilder()
    engineer = RaceEngineer()
    
    engineer.construct_car(builder)
    car = builder.get_result()
    
    assert isinstance(car, F1Car)
    assert "Low Drag" in car.front_wing
    assert "Low Drag" in car.rear_wing
    assert "Hard" in car.tires
    assert "Monza" in car.chassis

def test_builder_reset_mechanism():
    """
    TEST 3: State Management
    Ensures the builder resets correctly so we don't 'leak' parts 
    from a previous build into a new car.
    """
    builder = MonacoBuilder()
    engineer = RaceEngineer()
    
    # Build first car
    engineer.construct_car(builder)
    car1 = builder.get_result()
    
    # Build second car immediately
    engineer.construct_car(builder)
    car2 = builder.get_result()
    
    # They should be distinct objects
    assert car1 is not car2
    assert car1.chassis == car2.chassis

def test_partial_build_integrity():
    """
    TEST 4: Product Defaults
    Ensures a fresh F1Car starts with empty or None attributes 
    before the builder starts working.
    """
    car = F1Car()
    assert car.engine is None
    assert car.tires is None

def test_show_specs_output(capsys):
    """
    TEST 5: Product Method Functionality
    Validates that the show_specs method prints a correctly formatted string 
    with decorative borders.
    """
    car = F1Car(
        chassis="Test Chassis",
        engine="Test Engine",
        front_wing="Test Front Wing",
        rear_wing="Test Rear Wing",
        tires="Test Tires"
    )
    
    car.show_specs()
    captured = capsys.readouterr()
    
    assert "--- F1 Car Configuration ---" in captured.out
    assert "Chassis:    Test Chassis" in captured.out
    assert "---------------------------" in captured.out

def test_builder_initialization():
    """
    TEST 6: Immediate Readiness
    Ensures the builder initializes a car object upon instantiation so that 
    individual build methods can be called without prior manual reset.
    """
    builder = MonacoBuilder()
    # This should not raise an AttributeError even if construct_car wasn't called
    try:
        builder.build_tires()
    except AttributeError:
        pytest.fail("Builder was not initialized with a car instance in __init__.")

def test_inheritance_and_dry_reset():
    """
    TEST 7: DRY Reset Principle
    Verifies that the reset logic is correctly handled by the base class 
    and shared across concrete builders.
    """
    builder = MonzaBuilder()
    builder.build_chassis()
    builder.reset()         
    
    car = builder.get_result()
    assert car.chassis is None