import csv
from csv import DictReader

with open('ex2-text.csv', 'r') as file:
    dict_reader=DictReader(file)
    employees=list(dict_reader)
    print(employees)
file.close()

