def count_characters(input_string):
    uppercase_count = 0
    lowercase_count = 0
    number_count = 0

    for char in input_string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char.isdigit():
            number_count += 1

    return uppercase_count, lowercase_count, number_count

input_string = input("Enter a string: ")

result_tuple = count_characters(input_string)

print(f"{result_tuple}")