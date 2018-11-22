class TreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        # store the number of left child for each tree Node
        self.num_of_left = 0

        # store the max height difference
        self.max_diff = float('-inf')
        self.max_diff_node = None