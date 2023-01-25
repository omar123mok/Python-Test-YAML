import yaml

from Code.checks_yaml import validate_values, validate_keys


def main():
    count = 0
    with open("data.yaml", 'r') as x:
        data = yaml.safe_load(x)
    for x in data:
        print(validate_keys(x, count))
        print(validate_values(x, count))
        count += 1


if __name__ == "__main__":
    main()
