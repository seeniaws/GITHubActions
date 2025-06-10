from src.mathOperations import add, sub
def test_Add():
    assert add(2,3) == 5    
    assert add(-1,1) == 0
def test_Sub():    
    assert sub(2,3) ==-1
    assert sub(3,2) == 1
    
