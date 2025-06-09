from src.mathOperations import add, sub
def testAdd():
    assert add(2,3) == 5    
    assert add(-1,1) == 0
def testSub():    
    assert sub(2,3) ==-1
    assert sub(3,2) == 1
    