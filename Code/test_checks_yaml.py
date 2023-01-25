import pytest
import Code.checks_yaml as code

# Test data with valid input
valid_data = [{'firstname': 'John', 'lastname': 'Doe', 'gender': 'male', 'tags': ['student', 'programmer']}]

# Test data with invalid input (missing keys and values)
invalid_data = [{'firstname': '', 'lastname': '', 'gender': '', 'tags': []}]


def test_validate_keys_valid_input():
    print(valid_data)
    for x in valid_data:
        assert code.validate_keys(x, 1) == "All required keys are present for data at list index 1"


def test_validate_keys_invalid_input():
    with pytest.raises(AssertionError):
        for x in invalid_data:
            code.validate_keys(x, 1) == "The following keys are missing: ['firstname', 'lastname', 'gender', " \
                                               "'tags'] for data at list 1"


def test_validate_values_valid_input():
    for x in valid_data:
        assert code.validate_values(x, 1) == "All values are present for data at list index 1"


def test_validate_values_invalid_input():
    with pytest.raises(AssertionError):
        for x in invalid_data:
            code.validate_values(x, 1) == "The following values are missing: {'firstname': 'Value is missing', " \
                                                 "'lastname': 'Value is missing', 'gender': 'Value is missing', " \
                                                 "'tags': 'Value is missing'} for data at list 1"
