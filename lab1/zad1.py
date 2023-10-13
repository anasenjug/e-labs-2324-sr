def count_evens(numbers):
    evens = [num for num in numbers if num % 2 == 0]
    return len(evens)

input_numbers = input("Enter comma-separated integers: ")

numbers_list = [int(num) for num in input_numbers.split(',')]

num_of_evens = count_evens(numbers_list)
print(f"The number of even integers is: {num_of_evens}")