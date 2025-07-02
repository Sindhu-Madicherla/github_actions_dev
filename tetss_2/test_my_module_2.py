from src.my_module import add, subtract

def test_add_1():
    assert add(2, 3) == 5

def test_subtract_1():
    assert subtract(5, 3) == 1
