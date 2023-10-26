""""Read section 7.2 from the tutorial.
Read string methods documentation:
https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
https://docs.python.org/3/library/stdtypes.html#string-methods
Give special focus to split() and strip() methods

Write a simple program which loads the data from the .csv file (hint
about csv file format and writes it to different files
Read data from file ex2-text.csv
Parse it (split lines on , chars and store in variables)
Write data to files:
ex2-employees.txt in format employee,job title
ex2-locations.txt in format employee,office
Save your solution as ex2.py and commit, along with created .txt
files, all in the same commit."""
import csv
rows = []
with open('ex2-text.csv', 'r') as file:
    csvreader = csv.reader(file,delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        rows.append(row)


with open('ex2-employees.txt', 'w') as employeefile, open('ex2-locations.txt', 'w') as locationfile:
    for row in rows:
        employee, job_title, _, office = row 

        employeefile.write(f"{employee},{job_title}\n")

        locationfile.write(f"{employee},{office}\n")

print("Data has been written to ex2-employees.txt and ex2-locations.txt.")