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

    # get height of a tree
    def __get_height(self, root):
        if not root:
            return 0

        l_height = self.__get_height(root.left)
        r_height = self.__get_height(root.right)

        return max(l_height, r_height) + 1

    def get_height(self):
        return self.__get_height(self.__root)

    # get the number of nodes in a tree
    def __get_count(self, root):
        if not root:
            return 0

        l_count = self.__get_count(root.left)
        r_count = self.__get_count(root.right)

        return l_count + r_count + 1

    def get_count(self):
        return self.__get_count(self.__root)

    # get the num of left child for each node
    def __get_num_of_left(self, root):
        if not root:
            return 0

        l_count = self.__get_num_of_left(root.left)
        root.num_of_left = l_count
        r_count = self.__get_num_of_right(root.right)

        return l_count + r_count + 1

    def get_num_of_left(self):
        return self.__get_num_of_left(self.__root)

    # find the node with max difference in total number of descendent in its both subtrees
    def __node_diff(self, root):
        if not root:
            return 0

        l_nodes = self.__node_diff(root.left)
        r_nodes = self.__node_diff(root.right)

        diff = abs(r_nodes - l_nodes)
        if diff > self.max_diff:
            self.max_diff = diff
            self.max_diff_node = root

        return l_nodes + r_nodes + 1

    def node_diff(self):
        return self.__node_diff(self.__root)

    # find the minimum depth of a tree. The minimum depth is the number of nodes along he shortest
    # path from the root node down to the nearest leaf node
    def __find_min_depth(self, root):
        # corner case, handle the none node
        if not root:
            return 0

        # base case, choose leaf as base case
        if not root.left and not root.right:
            return 1

        # recursive step, set the none node's height to positive infinity to handle the nodes
        # that only have one side of sub-child like: 3(root) -> 5(left) -> None(right)
        l_min = self.__find_min_depth(root.left) if root.left else float('inf')
        r_min = self.__find_min_depth(root.right) if root.right else float('inf')

        return min(l_min, r_min) + 1

    def find_min_depth(self):
        return self.__find_min_depth(self.__root)

    # Lowest common ancestor
    def __LCA(self, root, node1, node2):

        if root is None or root == node1 or root == node2:
            return root

        l_node = self.__LCA(root.left, node1, node2)
        r_node = self.__LCA(root.right, node1, node2)

        if l_node and r_node:
            return root

        return l_node if l_node else r_node

    def LCA(self, node1, node2):
        return self.__LCA(self.__root, node1, node2)

'''
               5  
           4       11 
        3       8       12
             6     11.5     13
                7      12.5     14
'''
bst = BinarySearchTree()
values = [5, 4, 11, 3, 8, 12, 6, 11.5, 13, 7, 12.5, 14]
#values = [3, 9, 2, 5, 15, 7]
for val in values:
    bst.insert(val)
y = bst.pre_order()
print(y)
x = bst.in_order()
print(x)

balanced = bst.is_balance()
print(balanced)


print(bst.get_height())
print(bst.get_count())
print(bst.find_min_depth())

node1 = bst.query(11.5)
node2 = bst.query(12.5)
lca = bst.LCA(node1, node2)
print(lca.value)

# bst.delete(11)
# bst.pre_order()