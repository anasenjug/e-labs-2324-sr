import csv
import json

from csv import DictReader

with open('ex2-text.csv', 'r') as file:
    dict_reader=DictReader(file)
    employees=list(dict_reader)
file.close()

with open('ex4-employees.json', 'w', encoding='utf-8') as f:
    json.dump(employees, f)
