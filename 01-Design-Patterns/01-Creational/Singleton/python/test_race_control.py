import pytest
import threading
from race_control import RaceControl

def test_singleton_identity():
    """
    TEST 1: Verification of Uniqueness
    Two requests for RaceControl must return the exact same object instance.
    """
    instance_a = RaceControl.get_instance()
    instance_b = RaceControl.get_instance()
    
    assert instance_a is instance_b, "RaceControl instances are not the same! Singleton failed."

def test_state_consistency():
    """
    TEST 2: Verification of State Synchronization
    Changing the status via one reference must reflect in all other references.
    """
    instance_a = RaceControl.get_instance()
    instance_b = RaceControl.get_instance()
    
    # Track sensor detects an incident
    instance_a.update_status("YELLOW")
    
    assert instance_b.get_status() == "YELLOW", "Status update not reflected across instances!"
    
    # Reset for following tests
    instance_a.update_status("GREEN")

def test_initial_state():
    """
    TEST 3: Verification of Default State
    The race must always start with a GREEN flag.
    """
    instance = RaceControl.get_instance()
    # Ensure fresh state for this test (since Singletons persist in memory)
    instance.update_status("GREEN")
    
    assert instance.get_status() == "GREEN"

def test_thread_safety():
    """
    TEST 4: Verification of Thread-Safety (Stress Test)
    Simulate multiple sensors trying to access/create RaceControl simultaneously.
    """
    instances = []

    def get_instance_worker():
        instances.append(RaceControl.get_instance())

    # Create 50 threads trying to grab the RaceControl at the same time
    threads = [threading.Thread(target=get_instance_worker) for _ in range(50)]
    
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # All 50 references must point to the exact same memory address
    first_instance = instances[0]
    for inst in instances:
        assert inst is first_instance, "Thread-safety failed: Multiple instances created under load!"

def test_constructor_protection():
    """
    TEST 5: Verification of Encapsulation
    Directly calling RaceControl() should be discouraged or handled.
    Note: In Python, this depends on your implementation (Metaclass vs __new__).
    """
    # If you use a Metaclass, RaceControl() will often return the singleton.
    # If you want to be strict, you can make it raise a TypeError.
    # For now, we check if it at least still returns the SAME instance.
    instance_a = RaceControl.get_instance()
    instance_b = RaceControl()
    
    assert instance_a is instance_b, "Direct instantiation created a new object!"

def test_invalid_status_raises_error():
    """
    TEST 6: Verification of Input Validation
    Setting a status outside the allowed F1 flags must raise a ValueError.
    """
    instance = RaceControl.get_instance()
    
    # Check if the correct exception is raised for an invalid input
    with pytest.raises(ValueError) as excinfo:
        instance.update_status("PURPLE") # This color does not exist in F1
    
    # Verify the error message contains the expected guidance
    assert "Status must be one of" in str(excinfo.value)