def test_01():
 x = "this"
 assert 'h' in x

def test_02():
 x = "xythis"
 assert 'x' in x

def test_03():
 x = "xythis"
 assert 'y' in x

def add(a,b):
 return a+b

def test_add():
 assert add(1,1) == 2