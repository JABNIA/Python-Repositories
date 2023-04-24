from Final import validate
from Final import user_answer


def test_validate():
    assert validate("Wellington") == True
    assert validate("Mercury") == True
    assert validate("Call of duty") == True    
    assert validate("Hirohito") == True
    assert validate("Constantinople") == True
    assert validate("Troy") == False
    assert validate("Battlefield") == False
    assert validate("Oda nobunaga") == False

 