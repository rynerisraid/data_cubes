import sqlalchemy

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4
    
    
def test_sqlalchemy():
    assert sqlalchemy.__version__ == '2.0.12'