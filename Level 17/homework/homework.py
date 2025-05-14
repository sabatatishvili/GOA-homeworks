def manual_remove(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            del lst[i]
            return 
    return "Element not found"

def manual_index(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return "Element not found"

def manual_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

def manual_pop(lst, index=-1):
    if index < 0:
        index = len(lst) + index 
    if 0 <= index < len(lst):
        return lst.pop(index)
    return "Index out of range"

def manual_reverse(lst):
    right, left = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left -= 1
        right += 1
    return lst

list = [1, 2, 3, 4, 5]
manual_remove(list, 3)
print("After manual_remove:", list)
print("Index of 4:", manual_index(list, 4))
print("Length of list:", manual_len(list))
print("Popped element:", manual_pop(list))
print("List after manual_pop:", list)
manual_reverse(list)
print("List after manual_reverse:", list)