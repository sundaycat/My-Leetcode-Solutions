class TreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        # store the number of left child for each tree Node
        self.num_of_left = 0