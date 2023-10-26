#Write a simple program which asks the user for their name and prints the greeting to the user (Hi Name!)
#in the three string interpolation ways described in the section:
#using the formatted string literals method (7.1.1)
#using the String format() method (7.1.2)
#using the old string formatting method (7.1.4)
#Save your solution as ex1.py and commit

name=input("Please input your name")

print(f'Hi {name}!')

print('Hi {}!'.format(name))

print('Hi %s!' % name)