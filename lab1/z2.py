# Ask the user for a number. Depending on whether the number is even
# or odd, print out an appropriate message to the user.

num = int(input("Unesi djeljenik: "))
check = int(input("Unesi djelitelj: "))

if num % check == 0:
    print(f"broj {num} je djeljiv sa {check}")
else: 
    print(f"Broj {num} nije dijeljiv sa {check}")


print("Ovo je sve izvan ifa")

