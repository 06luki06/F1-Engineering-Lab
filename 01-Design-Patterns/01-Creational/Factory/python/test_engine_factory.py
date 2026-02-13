import pytest
from abc import ABC
from engine_factory import EngineFactory, FerrariEngine, MercedesEngine, Engine

def test_interface_enforcement():
    """
    TEST 0: Pythonic Interface Contract
    Ensures that the implementation uses the modern 'abc' module.
    """
    # 1. Ensure Engine inherits from ABC (Abstract Base Class)
    assert issubclass(Engine, ABC), "Engine class must inherit from abc.ABC!"
    
    # 2. Ensure Engine is genuinely abstract and cannot be instantiated
    # This forces the use of @abstractmethod decorator on methods
    with pytest.raises(TypeError):
        _ = Engine() 
    
    # 3. Check if abstract methods are marked as abstract
    assert getattr(Engine.start, '__isabstractmethod__', False), "The 'start' method must be decorated with @abstractmethod!"
    assert getattr(Engine.stop, '__isabstractmethod__', False), "The 'stop' method must be decorated with @abstractmethod!"
    assert getattr(Engine.get_spec, '__isabstractmethod__', False), "The 'get_spec' method must be decorated with @abstractmethod!"

def test_factory_creates_ferrari():
    """
    TEST 1: Ferrari Instantiation
    The factory must return an instance of FerrariEngine when requested.
    """
    factory = EngineFactory()
    engine = factory.get_engine("Ferrari")
    
    assert isinstance(engine, FerrariEngine)
    assert isinstance(engine, Engine)

def test_factory_creates_mercedes():
    """
    TEST 2: Mercedes Instantiation
    The factory must return an instance of MercedesEngine when requested.
    """
    factory = EngineFactory()
    engine = factory.get_engine("Mercedes")
    
    assert isinstance(engine, MercedesEngine)

def test_engine_behavior():
    """
    TEST 3: Polymorphism Check
    """
    factory = EngineFactory()
    ferrari = factory.get_engine("Ferrari")
    mercedes = factory.get_engine("Mercedes")
    
    assert ferrari.start() != mercedes.start()
    assert "Ferrari" in ferrari.get_spec()
    assert "Mercedes" in mercedes.get_spec()

def test_unknown_manufacturer_raises_error():
    """
    TEST 4: Error Handling
    """
    factory = EngineFactory()
    
    with pytest.raises(ValueError) as excinfo:
        factory.get_engine("Trabi")
    
    assert "Unknown manufacturer" in str(excinfo.value)

def test_engine_stop_method():
    """
    TEST 5: Stop Method Coverage
    Ensures that the 'stop' method is implemented and returns a sensible value
    for all concrete engine classes created by the factory.
    """
    factory = EngineFactory()
    ferrari = factory.get_engine("Ferrari")
    mercedes = factory.get_engine("Mercedes")
    ferrari_stop_result = ferrari.stop()
    mercedes_stop_result = mercedes.stop()
    # Ensure that calling stop() does not raise and returns a string (or at least a truthy value)
    assert isinstance(ferrari_stop_result, str)
    assert isinstance(mercedes_stop_result, str)
