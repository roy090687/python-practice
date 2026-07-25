# 2 different ways
def move_to_end_number(lst, element):
    if element in lst:
        lst.remove(element) # remove the element first
        lst.append(element) # append the same at the end

    return lst

def move_to_end_string(lst, element):
    if element in lst:
        idx = lst.index(element)
        value = lst.pop(idx) # remove the element first
        lst.append(value) # append the same at the end

    return lst

# Example
numbers = [2, 3, 4, 7, 9]
print("Number-Original one: ", numbers)
print("Number-After moving to end: ", move_to_end_number(numbers, 3))

names = ["Ajay", "Rahul", "Priya", "Ankita", "Vivek"]
print("String-Original one: ", names)
print("String-After moving to end: ", move_to_end_string(names, "Priya"))


