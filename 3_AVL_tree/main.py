from avl import *
import random

#array = random.sample(range(1, 1000), 20)
#print(array)

#given array: [601, 201, 223, 571, 142, 97, 658, 869, 188, 903, 954, 485, 88, 656, 982, 784, 847, 204, 402, 349]

array = [601, 201, 223, 571, 142, 97, 658, 869, 188, 903, 954, 485, 88, 656, 982, 784, 847, 204, 402, 349]

tree = Avl()
for i in array:
    tree.insert(i)
tree.preorder(tree.root)
#result: 223, 142, 97, 88, 201, 188, 204, 658, 485, 402, 349, 601, 571, 656, 869, 784, 847, 954, 903, 982,
print("\n")

temp = tree.findValue(142)
tree.removeElement(temp)
temp = tree.findValue(402)
tree.removeElement(temp)
temp = tree.findValue(223)
tree.removeElement(temp)


tree.preorder(tree.root)
print("\n")
#result: 204, 97, 88, 201, 188, 658, 485, 349, 601, 571, 656, 869, 784, 847, 954, 903, 982, 


temp = tree.findPredecessor(tree.findValue(784))
print(temp.value)
print("\n")
#result: 658

tree.removeChildren(temp)
tree.preorder(tree.root)
#result: 204, 97, 88, 201, 188, 658