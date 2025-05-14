#def manual_sum(numbers):
#    total = 0
#    for num in numbers:
#        total += num
#    return total
#nums = [15, 20, 45]
#result = manual_sum(nums)
#print(result)




def manual_append(listn, value):
    listn += [value]
    return listn
nums = [6, 8, 13]
manual_append(nums, 15)
print(nums)