


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

    def checkBalance(self, node):

        """
        example without recursion

        stack=[]
        levels={}

        stack.append(node)
        num = 0

        while stack:
            curr = stack.pop()
            if levels[curr] == None:
                num += 1
                levels[curr] = num

                if curr.left:
                    levels[curr.left] = num + 1
                    stack.append(curr.left)
                if curr.right:
                    levels[curr.right] = num + 1
                    stack.append(curr.right)
            else:
                num = levels[curr]

                if curr.left:
                    levels[curr.left] = num + 1
                    stack.append(curr.left)
                if curr.right:
                    levels[curr.right] = num + 1
                    stack.append(curr.right)

        max = max (set(levels.values()))
        min = min (set(levels.values()))

        return max-min >= 1
    """
    




