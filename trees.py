# Create node and tree class


class Node(object):
    def __init__(self, data, children=None):
        self.data = data
        if children is None:
            self.children = []
        else:
            self.children = children

    def addchildren(self, node, children = None):
        """adds Node to Tree"""
        self.children.append(Node(node))

    def __repr__(self):
        return "<Node {data}>".format(data = self.data)


class Tree(object):
    """creates Tree object"""
    def __init__(self, root):
        self.root = root

    def __repr__(self):
        """visibe representation of tree"""

        return "<Tree root={root}>".format(root = self.root)



    def findNode(self, node):
        curr = self.root
        stack = [curr]

        while curr != node:
            # print('does not equal to node!!!!!!')
            # print('curr.children====>', curr.children)
            if curr.children != []:
                for child in curr.children:
                    # print('child ****', child)
                    if child.data == node:
                        return child
                stack.pop()
                stack.append(curr.children)
                curr = stack[-1]

            else:
                raise Exception("Node not found.")

        return curr




testTree = Tree(Node('parent'))

testTree.root.addchildren('child1')
testTree.root.addchildren('child2')

node = testTree.findNode('child2')
node.addchildren('child2.1')
node.addchildren('child2.2')








# build a tree
