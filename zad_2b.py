# Petla For
numbers_1 = [5,7,2,9,6]
constant= 2
def multiply_1(list,f):
    iloczyn_1 = []
    for number in list:
        result = number * f
        iloczyn_1.append(result)
    return iloczyn_1
print(multiply_1(numbers_1,constant))

# Lista Skladana
numbers_2 = [5,7,2,9,6]
constant_2= 2
def multiply_2(list_2,f_2):
    return [number_2*f_2 for number_2 in list_2]
print(multiply_2(numbers_2,constant_2))