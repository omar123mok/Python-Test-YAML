[![validate](https://github.com/omar123mok/Python-Test-YAML/actions/workflows/validate.yml/badge.svg)](https://github.com/omar123mok/Python-Test-YAML/actions/workflows/validate.yml)

[![Pull validate](https://github.com/omar123mok/Python-Test-YAML/actions/workflows/validate.yml/badge.svg?event=pull_request)](https://github.com/omar123mok/Python-Test-YAML/actions/workflows/validate.yml)


# Data Validation
This repository contains a validation script and GitHub Actions workflow to validate data in a YAML file.

# File Structure
data.yaml: Example YAML file containing data to be validated.
test_validation.py: Python script that validates data in the YAML file.
.github/workflows/validate.yaml: GitHub Actions workflow that runs the validation script on push.
Script Functionality
The validation script test_validation.py contains a function func1(data) that checks for the presence of the following keys and values in each item of the data:

'First Name'
'Last Name'
'Gender'
'Tags'
If any of these keys or values are missing, the script raises an assertion error with a message indicating which key or value is missing.

# Workflow Functionality
The GitHub Actions workflow validate.yaml runs on push and performs the following actions:

# Checkouts the repository.
Installs the necessary packages, pytest and pyyaml
Runs the validation script with the command pytest -k test_validation.py
