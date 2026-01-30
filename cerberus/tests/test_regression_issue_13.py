from cerberus import Validator

def test_nested_dict_schema_validation():
    schema = {
        'user': {
            'type': 'dict',
            'schema': {
                'name': {'type': 'string', 'required': True},
                'age': {'type': 'integer', 'min': 0}
            }
        }
    }
    v = Validator(schema)
    # This should FAIL — age is a string, not integer
    result = v.validate({'user': {'name': 'John', 'age': 'not_a_number'}})
    assert not result, "Validation should fail for invalid nested dict value."
    assert 'user' in v.errors, "Error should be reported for 'user' field."
    assert 'age' in v.errors['user'][-1], "Error should be reported for 'age' in nested dict."
    # This should PASS
    result2 = v.validate({'user': {'name': 'John', 'age': 42}})
    assert result2, "Validation should pass for valid nested dict."
