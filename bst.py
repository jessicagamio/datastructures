


class BST(object):
    """create Binary Search Tree"""
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None


    def validateBST(self, node, min = None, max = None):
        """Returns True if a Binary Search Tree"""

        if node == None:
            return True

        # add base case that breaks the function call if node doesn't comply with BST rules
        if min != None and node.data <= min or max != None and node.data > max:
            return False

        # call functions to each sub tree
        if node.left:
            validateBST(node.left,None,node.data)

        if node.right:
            validateBST(node.right,node.data,None)

        return True

    def checkBalance()