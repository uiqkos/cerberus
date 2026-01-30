from cerberus import Validator
import pytest

def test_nested_schema_invalid_inner():
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
    doc = {'user': {'name': 'John', 'age': 'not_a_number'}}
    result = v.validate(doc)
    assert not result, "Validation should fail for invalid nested dict"
    assert 'user' in v.errors, f"Expected error for 'user', got: {v.errors}"
    assert 'age' in v.errors['user'], f"Expected error for 'age', got: {v.errors['user']}"
    assert any('integer' in str(e) or 'type' in str(e) for e in v.errors['user']['age']), f"Expected type error for 'age', got: {v.errors['user']['age']}"

def test_nested_schema_valid():
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
    doc = {'user': {'name': 'John', 'age': 42}}
    result = v.validate(doc)
    assert result, f"Validation should pass for valid nested dict, got errors: {v.errors}"
