class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
    
    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)

        else:
            if self.right ==None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
    
    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
    
    def preorder_traversal(self):
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()
        
    def prosorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
    def find(self, value):
        if value > self.value:
            if self.left in None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else: 
                return self.right.find(value)
        else: 
            return True
        
