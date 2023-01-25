import pytest
import Code.checks_yaml as code

# Test data with valid input
valid_data = [{'firstname': 'John', 'lastname': 'Doe', 'gender': 'male', 'tags': ['student', 'programmer']}]

# Test data with invalid input (missing keys and values)
invalid_data_1 = [{'firstname': '', 'lastname': '', 'gender': ''}]
invalid_data_2 = [{'firstname': '', 'lastname': '', 'gender': '', 'tags': []}]


def test_validate_keys_valid_input():
    for x in valid_data:
        assert code.validate_keys(x, 1) == "All required keys are present for data at list index 1"


def test_validate_keys_invalid_input():
    with pytest.raises(AssertionError):
        for x in invalid_data_1:
            assert code.validate_keys(x, 1) == "All required keys are present for data at list index 1"

def test_validate_values_valid_input():
    for x in valid_data:
        assert code.validate_values(x, 1) == "All values are present for data at list index 1"


def test_validate_values_invalid_input():
    with pytest.raises(AssertionError):
        for x in invalid_data_2:
            assert code.validate_values(x, 1) == "All values are present for data at list index 1"
