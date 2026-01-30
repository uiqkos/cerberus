from cerberus import Validator

def test_regex_pr10():
    schema = {'code': {'type': 'string', 'regex': '[A-Z]{3}'}}
    v = Validator(schema)
    assert v.validate({'code': 'ABC'}), "'ABC' should match '[A-Z]{3}' and pass validation"
    assert not v.validate({'code': 'ABCD'}), "'ABCD' should not match '[A-Z]{3}' and fail validation"
    assert not v.validate({'code': 'abc'}), "'abc' should not match '[A-Z]{3}' and fail validation"
    assert not v.validate({'code': 'A1C'}), "'A1C' should not match '[A-Z]{3}' and fail validation"
    # Also test with anchors
    schema2 = {'code': {'type': 'string', 'regex': '^[A-Z]{3}$'}}
    v2 = Validator(schema2)
    assert v2.validate({'code': 'ABC'}), "'ABC' should match '^[A-Z]{3}$' and pass validation"
    assert not v2.validate({'code': 'ABCD'}), "'ABCD' should not match '^[A-Z]{3}$' and fail validation"
    assert not v2.validate({'code': 'abc'}), "'abc' should not match '^[A-Z]{3}$' and fail validation"
    assert not v2.validate({'code': 'A1C'}), "'A1C' should not match '^[A-Z]{3}$' and fail validation"
