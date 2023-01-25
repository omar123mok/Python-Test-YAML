required_keys = ["firstname", "lastname", "gender", "tags"]


def validate_keys(data, count):
    missing_keys = []
    data_keys = []
    # print(data)
    for k in data.keys():
        k = k.replace(" ", "")
        k = k.lower()
        data_keys.append(k)
    # print(data_keys)
    for key in required_keys:
        if key not in data_keys:
            missing_keys.append(key)
    if len(missing_keys) > 0:
        return f"The following keys are missing: {missing_keys} for data at list {count}"
    else:
        return f"All required keys are present for data at list index {count}"


def validate_values(data, count):
    missing_values = {}
    for key, value in data.items():
        if not value:
            missing_values[key] = "Value is missing"
    if len(missing_values) > 0:
        return f"The following values are missing: {missing_values} for data at list {count}"
    else:
        return f"All values are present for data at list index {count}"

