from src.mypkg.app import say_hello

def test_say_hello():
    assert say_hello() == 'hello'
