import random
import sys

def generateList(length, upper_bound):
    list_1 = []
    for i in range(length):
        list_1.append(random.randint(0, upper_bound))
    return list_1

def binarySearchToLeftBound(list_1, l_index, r_index, value):
    middle = -1
    while(1):
        if(l_index == r_index):
            break
        else:
            middle = (l_index + r_index) // 2
            if(list_1[middle] < value):
                l_index = middle + 1
            else:
                r_index = middle
    if(list_1[l_index] == value):
        return l_index
    else:
        sys.exit("That value does not occur in the given list.")

def binarySearchToRightBound(list_1, l_index, r_index, value):
    middle = -1
    while(1):
        if(l_index == r_index):
            break
        else:
            middle = ((l_index + r_index) // 2) + 1
            if(list_1[middle] <= value):
                l_index = middle
            else:
                r_index = middle - 1
    if(list_1[l_index] == value):
        return r_index
    else:
        sys.exit("That value does not occur in the given list.")

def findOccurencies(list_1, length, value):
    left = binarySearchToLeftBound(list_1, 0, length - 1, value)
    right = binarySearchToRightBound(list_1, 0, length - 1, value)
    print("Value ", value, " appeared on positions between ", left, " and ", right, " (bounds included)")
    print("That gives you ", right - left + 1, " occurrences in total.")


#########################################################################################################
print("Enter the length of your list: ")
while(1):
    try:
        list_length = int(input())
    except:
        print("You must enter a number! (You know, that mathematical thing without letters)")
        continue
    if(list_length <= 0):
        print("Positive integers only.")
        continue
    break

print("...and your upper bound to generate values: ")
while(1):
    try:
        upper_bound = int(input())
    except:
        print("You must enter a number! (You know, that mathematical thing without letters)")
        continue
    if(upper_bound <= 0):
        print("Higher than 0 integers only.")
        continue
    break

list_1 = generateList(list_length, upper_bound)
list_1.sort()

print("\nGenerated list: ", list_1, "\nEnter a number from 0 to", upper_bound)
while(1):
    try:
        searched_number = int(input())
    except:
        print("You must enter a number! (You know, that mathematical thing without letters)")
        continue
    if(searched_number > upper_bound or searched_number < 0):
        print("Your number must be not higher than upper bound and not lower than 0.")
        continue
    break
findOccurencies(list_1, list_length, searched_number)
