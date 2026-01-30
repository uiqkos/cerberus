from cerberus import Validator
import pytest

def test_if_field_conditional_validation():
    schema = {
        'payment_method': {'type': 'string', 'allowed': ['card', 'cash']},
        'card_number': {
            'type': 'string',
            'if_field': {
                'field': 'payment_method',
                'value': 'card',
                'then': {'required': True, 'regex': '^[0-9]{16}$'}
            }
        }
    }
    v = Validator(schema)

    # payment_method is 'card', so card_number is required and must match regex
    assert v.validate({'payment_method': 'card', 'card_number': '1234567890123456'}) is True
    assert v.validate({'payment_method': 'card'}) is False
    assert 'card_number' in v.errors
    # payment_method is 'cash', so card_number rules don't apply
    assert v.validate({'payment_method': 'cash'}) is True
    assert v.validate({'payment_method': 'cash', 'card_number': 'invalid'}) is True

    # Nested document test
    schema_nested = {
        'payment': {
            'type': 'dict',
            'schema': {
                'method': {'type': 'string', 'allowed': ['card', 'cash']},
                'card_number': {
                    'type': 'string',
                    'if_field': {
                        'field': 'method',
                        'value': 'card',
                        'then': {'required': True, 'regex': '^[0-9]{16}$'}
                    }
                }
            }
        }
    }
    v2 = Validator(schema_nested)
    # method is 'card', so card_number required
    assert v2.validate({'payment': {'method': 'card', 'card_number': '1234567890123456'}}) is True
    assert v2.validate({'payment': {'method': 'card'}}) is False
    # method is 'cash', so card_number rules don't apply
    assert v2.validate({'payment': {'method': 'cash'}}) is True
    assert v2.validate({'payment': {'method': 'cash', 'card_number': 'invalid'}}) is True
