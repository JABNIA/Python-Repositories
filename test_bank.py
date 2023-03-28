from bank import variants

def test_Hello():
    assert variants("Hello") == "$0"
    assert variants("hello") == "$0"
def test_on_h():
    
    assert variants("hi") == "$20"
    assert variants("hey") == "$20"

def test_other():
    assert variants("Welcome") == "$100"
    assert variants("Good morning") == "$100"
    assert variants("Greetings") == "$100"
    assert variants("Good day") == "$100"
    assert variants("Good evening") == "$100"