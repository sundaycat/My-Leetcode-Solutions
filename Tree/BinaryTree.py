from TreeNode import TreeNode


class BinarySearchTree(object):

    def __init__(self):
        self.__root = None

    # root => left => right
    def __pre_order(self, root, rs):
        if root:
            rs.append(root.value)
            self.__pre_order(root.left, rs)
            self.__pre_order(root.right, rs)

    def pre_order(self):
        rs = []
        self.__pre_order(self.__root, rs)
        return rs

    # left => root => right
    def __in_order(self, root, rs):
        if root:
            self.__in_order(root.left, rs)
            rs.append(root.value)
            self.__in_order(root.right, rs)

    def in_order(self):
        rs = []
        self.__in_order(self.__root, rs)
        return rs

    # check if the binary tree is a balanced tree(diff <= 1)
    def __is_balanced(self, root):

        if not root:
            return 0

        l_height = self.__is_balanced(root.left)
        r_height = self.__is_balanced(root.right)

        diff = abs(l_height - r_height)
        if diff > 1 or l_height == -1 or r_height == -1:
            return -1

        return max(l_height, r_height) + 1

    def is_balance(self):
        return self.__is_balanced(self.__root) != -1

    # query the BST for given values, return the corresponding node
    def __query(self, root, value):

        # if the value doesn't contain in BST, then return None
        if root is None:
            return None

        if root.value == value:
            return root
        elif root.value > value:
            return self.__query(root.left, value)
        else:
            return self.__query(root.right, value)

    def query(self, value):
        return self.__query(self.__root, value)

    # insert a new node to the binary search tree
    def __insert(self, root, value):
        if not root:
            root = TreeNode(value)

        if root.value > value:
            root.left = self.__insert(root.left, value)
        elif root.value < value:
            root.right = self.__insert(root.right, value)
        else:
            root.value = value

        return root

    def insert(self, value):
        self.__root = self.__insert(self.__root, value)

    def __get_min_parent(self, root):
        if root is None:
            return None

        while root.left.left:
            root = root.left

        return root

    # delete a node from the tree
    def __delete(self, root, value):

        if not root:
            return None

        if root.value == value:

            # the current node's right child is None, ex, delete node 4
            if root.left and not root.right:
                root = root.left
            elif root.right and not root.left:
                root = root.right
            else:

                # if the delete node is the parent node of the left most node
                if root.right.left is None:
                    root.right.left = root.left
                    root = root.right
                else:
                    # obtain the left most node of the right subtree
                    new_root_parent = self.__get_min_parent(root.right)
                    new_root = new_root_parent.left

                    # assign the new root's original right child to its parent's left child
                    new_root_parent.left = new_root.right

                    # assign the current root's left and right child to the new root
                    new_root.left = root.left
                    new_root.right = root.right

                    # make the new root point to the current root
                    root = new_root

        elif root.value > value:
            root.left = self.__delete(root.left, value)

        elif root.value < value:
            root.right = self.__delete(root.right, value)

        return root

    def delete(self, value):
        self.__root = self.__delete(self.__root, value)

    '''
    Given a binary tree, write a function to determine whether this tree is a binary search tree
    '''
    def is_bst(self):
        # if the tree is None, then return true
        if self.__root is None:
            return True

        # initialize the variables lower and upper to be the max and min of the current system the
        lower = float("-inf")
        upper = float("inf")

        return self.__helper(self.__root, lower, upper)

    def __helper(self, root, lower, upper):
        # stop when we at the bottom of the tree, none are treated as -inf and inf
        if root is None:
            return True

        # stop when the node value is out of the range (lower, upper)
        # Don't allow duplicate tree nodes
        if root.value <= lower or root.value >= upper:
            return False

        # recursively iterate the whole tree
        is_bst_left = self.__helper(root.left, lower, root.value)
        is_bst_right = self.__helper(root.right, root.value, upper)

        return is_bst_left and is_bst_right


"""
               5  
           4       11 
        3       8       12
             6     11.5     13
                7      12.5     14
"""
bst = BinarySearchTree()
values = [5, 4, 11, 3, 8, 12, 6, 11.5, 13, 7, 12.5, 14]
for val in values:
    bst.insert(val)
y = bst.pre_order()
print(y)
x = bst.in_order()
print(x)

balanced = bst.is_balance()
print(balanced)


# bst.delete(11)
# bst.pre_order()

def get_num_of_left(root):
    if root is None:
        return 0

    num_of_left = get_num_of_left(root.left)
    root.num_of_left = num_of_left
    num_of_right = get_num_of_left(root.right)

    return num_of_left + num_of_right + 1


# return the max difference in two subtrees.
max_diff = -1
res = None


def node_diff(root):
    global max_diff
    global res
    if root is None:
        return 0

    l_node = node_diff(root.left)
    r_node = node_diff(root.right)
    diff = abs(l_node - r_node)
    if diff > max_diff:
        max_diff = diff
        res = root

    return l_node + r_node + 1


# return the min_depth of a tree
def min_depth(root):
    if not root:
        return 0

    # choose leaf as base case
    if root.left is None and root.right is None:
        return 1

    # handle the nodes that only have one side of sub-child
    l_min = min_depth(root.left) if root.left else float('inf')
    r_min = min_depth(root.right) if root.right else float('inf')

    return min(l_min, r_min) + 1