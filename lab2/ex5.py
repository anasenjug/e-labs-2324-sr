import json

class Employee:

    def __init__(self, name, title, age, office):
        self.name = name
        self.title = title
        self.age = age
        self.office = office

    def __str__(self):
        return f"{self.name} ({self.age}), {self.title} @ {self.office}"

with open("ex4-employees.json", "r", encoding="utf-8") as f:
    employees = json.load(f)

employees_list=[]
for employee in employees:
    employees_list.append(Employee(employee["Employee"],employee["job title"],employee["age"],employee["office"]))

for e in employees_list:
    print(e)
