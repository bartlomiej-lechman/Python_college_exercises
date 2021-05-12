import random


def generateList(length, upper_bound):
    list_1 = []
    for i in range(length):
        list_1.append(random.randint(0, upper_bound))
    return list_1


def linearSearch(list_1, searched_value):
    occurences = []
    for i in range(len(list_1)):
        if list_1[i] == searched_value:
            occurences.append(i)
    return occurences

print("Enter length of your list: ")
list_length = int(input())
print("...and your upper bound to generate values: ")
upper_bound = int(input())

list_1 = generateList(list_length, upper_bound)
print("\nGenerated list: ", list_1, "\nEnter a number from 0 to", upper_bound)
searched_number = -1
while(1):
    searched_number = int(input())
    if(searched_number <= upper_bound):
        break
    else:
        print("Try again")
result = linearSearch(list_1, searched_number)
print("Your number occured ", len(result), " times and it occurs on positions: ", result)
