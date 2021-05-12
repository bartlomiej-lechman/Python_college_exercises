class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value
        self.balance = 0

class Avl:
    def __init__(self):
        self.root = None
        self.size = 0

    def removeChildren(self, node):
        """Removing subtree from given node without removing node itself"""
        node.left = None
        node.right = None

    def findPredecessor(self, node):
        """Returns a reference to the predecessor (element visited before in in-order traverse) if exists (given node is not the root)"""
        temp = None
        if(node):
            if(node.left):
                node = node.left
                while(node.right):
                    node = node.right
            else:
                temp = node
                node = node.parent
                while( node and (node.right is not temp) ):
                    temp = node
                    node = node.parent
        return node

    def findValue(self, value):
        """Helper function to find reference to a node with given value"""
        reference = self.root
        while( (reference) and (reference.value is not value) ):
            if (value < reference.value):
                reference = reference.left
            else:
                reference = reference.right
        return reference

    def removeElement(self, node):
        """Recursive removal of given node with perseverance internal structure"""
        nested = None
        n1, n2, n3 = None, None, None

        if(node.left and node.right):
            n2 = self.removeElement(self.findPredecessor(node))
            nested = False
        else:
            if node.left:
                n2 = node.left
                node.left = None
            else:
                n2 = node.right
                node.right = None
            node.balance = 0
            nested = True

        if n2:
            n2.parent = node.parent
            n2.left = node.left
            if n2.left:
                n2.left.parent = n2
            n2.right = node.right
            if n2.right:
                n2.right.parent = n2
            n2.balance = node.balance

        if node.parent:
            if (node.parent.left == node):
                node.parent.left = n2
            else:
                node.parent.right = n2
        else:
            self.root = n2

        if nested:
            n3 = n2
            n2 = node.parent
            while (n2):
                if not n2.balance:
                    if (n2.left == n3):
                        n2.balance = -1
                    else:
                        n2.balance = 1
                    break
                else:
                    if( ( (n2.balance == 1) and (n2.left == n3) ) or ( (n2.balance == -1) and (n2.right == n3) ) ):
                        n2.balance = 0
                        n3 = n2
                        n2 = n2.parent
                    else:
                        if (n2.left == n3):
                            n1 = n2.right
                        else:
                            n1 = n2.left
                        if not n1.balance:
                            if (n2.balance == 1):
                                self.__leftLeft(n2)
                            else:
                                self.__rightRight(n2)
                            break
                        elif (n2.balance == n1.balance):
                            if(n2.balance == 1):
                                self.__leftLeft(n2)
                            else:
                                self.__rightRight(n2)
                            n3 = n1
                            n2 = n1.parent
                        else:
                            if(n2.balance == 1):
                                self.__leftRight(n2)
                            else:
                                self.__rightLeft(n2)
                            n3 = n2.parent
                            n2 = n3.parent
        return node
            
    def __rightRight(self, n1):
        """Helper function to rotate right twice"""
        n2 = n1.right
        ref = n1.parent
        n1.right = n2.left

        if(n1.right):
            n1.right.parent = n1

        n2.left = n1
        n2.parent = ref
        n1.parent = n2

        if ref:
            if(ref.left == n1):
                ref.left = n2
            else:
                ref.right = n2
        else:
            self.root = n2

        if(n2.balance == -1):
            n1.balance = 0
            n2.balance = 0
        else:
            n1.balance = -1
            n2.balance = 1

    def __rightLeft(self, n1):
        """Helper function to rotate right then left"""
        n2 = n1.right
        n3 = n2.left
        ref = n1.parent
        n2.left = n3.right

        if n2.left:
            n2.left.parent = n2
        n1.right = n3.left
        if n1.right:
            n1.right.parent = n1

        n3.left = n1
        n3.right = n2
        n1.parent = n3
        n2.parent = n3
        n3.parent = ref

        if ref:
            if (ref.left == n1):
                ref.left = n3
            else:
                ref.right = n3
        else:
            self.root = n3

        if(n3.balance == -1):
            n1.balance = 1
        else:
            n1.balance = 0

        if(n3.balance == 1):
            n2.balance = -1
        else:
            n2.balance = 0

        n3.balance = 0

    def __leftLeft(self, n1):
        """Helper function to rotate left twice"""
        n2 = n1.left
        ref = n1.parent
        n1.left = n2.right

        if n1.left:
            n1.left.parent = n1

        n2.right = n1
        n2.parent = ref
        n1.parent = n2

        if ref:
            if (ref.left == n1):
                ref.left = n2
            else:
                ref.right = n2
        else:
            self.root = n2

        if(n2.balance == 1):
            n1.balance = 0
            n2.balance = 0
        else:
            n1.balance = 1
            n2.balance = -1

    def __leftRight(self, n1):
        """Helper function to rotate left then right"""
        n2 = n1.left
        n3 = n2.right
        ref = n1.parent

        n2.right = n3.left
        if n2.right:
            n2.right.parent = n2
        n1.left = n3.right
        if n1.left:
            n1.left.parent = n1

        n3.right = n1
        n3.left = n2
        n1.parent = n3
        n2.parent = n3
        n3.parent = ref

        if ref:
            if (ref.left == n1):
                ref.left = n3
            else:
                ref.right = n3
        else:
            self.root = n3

        if (n3.balance == 1):
            n1.balance = -1
        else:
            n1.balance = 0

        if (n3.balance == -1):
            n2.balance = 1
        else:
            n2.balance = 0

        n3.balance = 0

    def insert(self, value):
        """Add node with given value and restore the balance"""
        self.size = self.size + 1
        adding = Node(value)
        selector = self.root
        if not self.root:
            self.root = adding
            self.size = self.size + 1
        else:
            while(True):
                if(value < selector.value):
                    if not selector.left:
                        selector.left = adding
                        break
                    selector = selector.left
                else:
                    if not selector.right:
                        selector.right = adding
                        break
                    selector = selector.right
            adding.parent = selector

            
            if selector.balance:
                selector.balance = 0
            else:
                if (selector.left == adding):
                    selector.balance = 1
                else:
                    selector.balance = -1

                climber = selector.parent
                tester = False

                while (climber):
                    if climber.balance:
                        tester = True
                        break

                    if(climber.left == selector):
                        climber.balance = 1
                    else:
                        climber.balance = -1

                    selector = climber
                    climber = climber.parent

                if(tester):
                    if(climber.balance == 1):
                        if(climber.right == selector):
                            climber.balance = 0
                        elif (selector.balance == -1):
                            self.__leftRight(climber)
                        else:
                            self.__leftLeft(climber)
                    else:
                        if(climber.left == selector):
                            climber.balance = 0
                        elif (selector.balance == 1):
                            self.__rightLeft(climber)
                        else:
                            self.__rightRight(climber)

    def preorder(self, node):
        """Print values in preorder traveral"""
        print(node.value, end=", ")
        if node.left:
            self.preorder(node.left)
        if node.right:
            self.preorder(node.right)
            
