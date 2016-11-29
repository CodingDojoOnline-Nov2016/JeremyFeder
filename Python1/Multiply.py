#one solution
a = [2, 4, 10, 16]
def multiply(list, multiplier):
    multiplied_list = []
    for num in list:
        multiplied_list.append(num * multiplier)
    return multiplied_list

print multiply(a, 5)


#REALLY GOOD SOLUTION!!
a = [2, 4, 10, 16]

def multiply(list, val):
    multiplied_list = [i * val for i in list]
    return multiplied_list

print multiply(a, 5)
