import json

class Employee:

    def __init__(self, name, title, age, office):
        self.name = name
        self.title = title
        self.age = age
        self.office = office

    def __str__(self):
        return f"{self.name} ({self.age}), {self.title} @ {self.office}"


class Company:

    def __init__(self, name):
        self.name = name
        self.employees = []

    def __str__(self):
        return f"{self.name} ({len(self.employees)} employees)"

    def employ(self, name, title, age, office):
        new_employee = Employee(name, title, age, office)
        self.employees.append(new_employee)

    def fire(self, name):
        for e in self.employees:
            if e.name == name:
                self.employees.remove(e)

    def load_from_json(self, path_to_json):
        with open(path_to_json,"r",encoding="utf-8") as f:
            self.employees=json.load(f)

    def save_to_json(self, path_to_json):
        employee_list=[]
        for employee in self.employees:
            employee_list.append(employee.to_dict())

        with open(path_to_json,"w",encoding="utf-8") as f:
            json.dump({"employee_list":employee_list},f)

    def print_employees(self):
       for employee in self.employees:
           print(employee)


def main():
    nike = Company("Nike")
    print(nike)


    nike.employ("Homer Simpson", "CEO", 44, "Lobby")
    nike.employ("Marge Simpson", "CTO", 33, "Lobby")
    print(nike)

    nike.fire("Homer Simpson")
    print(nike)

    adidas = Company("Adidas")
    print(adidas)
    adidas.employ("Homer Simpson", "CEO", 44, "Lobby")
    adidas.employ("Marge Simpson", "CTO", 33, "Lobby")
    adidas.employ("Bart Simpson", "CEO", 44, "Lobby")
    adidas.employ("Lisa Simpson", "CTO", 33, "Lobby")
    print(adidas)

    adidas.print_employees()

    adidas.fire("Homer Simpson")
    adidas.fire("Marge Simpson")
    print(adidas)
    adidas.save_to_json("ex6-employees.json")

if __name__ == "__main__":
    main()
