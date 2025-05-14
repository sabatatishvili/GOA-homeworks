#list1 = [1, 2, 3]
#list2 = [4, 5, 6]
#comb_list = []
#for item in list1:
#    comb_list.append(item)
#for item in list2:
#    comb_list.append(item)
#print(comb_list)

#def rem_odds(numbers):
#    result = []
#    for num in numbers:
#        if num % 2 == 0: 
#            result.append(num)
#    return result
#nums = [5, 6, 7, 8, 9, 10, 11]
#print(rem_odds(nums))

def nums(nums):
    result = ""
    for num in nums:
        result += str(num) 
    return result
numbers = [5, 10, 30, 55]
print(nums(numbers))