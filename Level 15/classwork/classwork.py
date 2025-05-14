def divisible_numbers(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]


numbers_list = [1, 23, 165, 2, 3, 92, 10, 34, 911]
divisor = 3


number4_list = divisible_numbers(numbers_list, divisor)
print(number4_list)
