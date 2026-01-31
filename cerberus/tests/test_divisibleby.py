from cerberus import Validator

def test_divisibleby_rule():
    schema = {'quantity': {'type': 'integer', 'divisibleby': 5}}
    v = Validator(schema)

    assert v.validate({'quantity': 10})
    assert not v.validate({'quantity': 7})
    assert v.errors['quantity'][0] == 'value is not divisible by 5'
    assert v.validate({'quantity': 0})

    schema = {'quantity': {'type': 'integer', 'divisibleby': 3}}
    v = Validator(schema)
    assert v.validate({'quantity': 9})
    assert not v.validate({'quantity': 8})
    assert v.errors['quantity'][0] == 'value is not divisible by 3'
    assert v.validate({'quantity': 0})
