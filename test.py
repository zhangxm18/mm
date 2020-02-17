def test_01():
 x = "this"
 assert 'h' in x

def test_02():
 x = "hello"
 assert 'x' in x

def add(a,b):
 return a+b

def test_add():
 assert add(1,1) == 2