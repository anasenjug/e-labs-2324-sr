def has_adjacent_twos(numbers_list):
    for i in range(len(numbers_list) - 1):
        if numbers_list[i] == 2 and numbers_list[i + 1] == 2:
            return True
    return False


input_numbers = input("Enter comma-separated integers: ")


numbers_list = [int(num) for num in input_numbers.split(',')]


result = has_adjacent_twos(numbers_list)


print("Result:", result)