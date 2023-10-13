input_numbers = input("Enter comma-separated integers: ")


numbers_list = [int(num) for num in input_numbers.split(',')]

max_num = numbers_list[0]
min_num = numbers_list[0]
total_sum = 0

for num in numbers_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

    total_sum += num

centered_sum = total_sum - max_num - min_num
centered_avg = centered_sum // (len(numbers_list) - 2)

print("Centered Average:", centered_avg)