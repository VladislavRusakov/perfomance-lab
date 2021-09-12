from sys import argv
import json
from typing import Union


tests = argv[1]
values = argv[2]


with open(tests, 'r') as f:
    tests_json = json.load(f)


with open(values, 'r') as f:
    values_json = json.load(f)


def recursive_search(tests: Union[dict, list]) -> None:
    """"Рекурсивная функция поиска id в tests.json и добавления им value из values.json"""
    if type(tests) == dict:
        for instance in values_json['values']:
            if instance['id'] == tests['id']:
                tests['value'] = instance['value']
        if 'values' in tests:
            recursive_search(tests['values'])

    elif type(tests) == list:
        for instance in tests:
            recursive_search(instance)
        
recursive_search(tests_json['tests'])

with open('report.json', 'w') as f:
    json.dump(tests_json, f)


