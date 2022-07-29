# Implement AVLTree

class AVLNode(object):
    """Create a node"""
    
    def __init__(self, key: int) -> None:
        # The node's key
        self.key = key
        # The node's left child
        self.left = None
        # The node's right child
        self.right = None
        
    def __str__(self) -> str:
        "String representation" 
        return str(self.key)
        
             
class AVLTree(object):
    """An AVLTree""" 
    # The number of trees that form in avl
    N_Tree: int = 0
    
    def __init__(self) -> None:
        # Empty Tree (without root)
        self.root = None
        # The heihgt's tree
        self.height: int = 0
        # The difference between the height of the left and the right tree
        self.balance: int = 0
        
           
    def insert(self, key: int) -> None:
        """Insert new key into node"""
        node = AVLNode(key)
        # Initial tree
        if not self.root:
            self.root = node
            self.root.left = AVLTree()
            self.root.right = AVLTree()
            self.N_Tree += 1
        # Insert key to the left subtree    
        elif node.key < self.root.key:
            self.root.left.insert(node.key)
            self.N_Tree += 1
        # Insert key to the right subtree
        elif node.key > self.root.key:
            self.root.right.insert(node.key)
            self.N_Tree += 1
        
        self.update_height()
        self.update_balance()
        self.control_balance()
            
       
    def update_height(self) -> None:
        """
        Update tree height, tree height is max height of either left or right
        subtrees +1 for root of the tree
        """
        if self.root:
            if self.root.left:
                self.root.left.update_height()
            if self.root.right:
                self.root.right.update_height()
  
            self.height = 1 + max(self.root.left.height ,
                                  self.root.right.height)
        else:
            self.height = 0
            
                  
    def update_balance(self) -> None:
        """
        Tree balance factor, the balance factor is calculated as follows: 
        balance = height(left subtree) - height(right subtree). 
        """ 
        if self.root:
            if self.root.left:
                self.root.left.update_balance()
            if self.root.right:
                self.root.right.update_balance()
            self.balance = self.root.left.height - self.root.right.height
        else:
            self.balance = 0
            
            
    def control_balance(self) -> None:
        """
        Control_balance tree. After inserting or deleting a node, it is 
        necessary to check each of the node's ancestors for consistency with
        the rules of AVL( -1 <= balance <= 1 otherwise must to rotate)
        """
        # For each node checked, if the balance factor remains −1, 0, or +1
        # then no rotations are necessary.
        if self.root:
            # Conditions of breaking avl rules
            while self.balance > 1 or self.balance < -1:
                # Left subtree is larger than right subtree
                if self.balance > 1:
                    # Negative balance need LR rotation
                    if self.root.left.balance < 0:
                        self.root.left.rotate_left()
                        self.update_height()
                        self.update_balance()
                        self.N_Tree += 1
                    # Need R rotation    
                    self.rotate_right()
                    self.update_height()
                    self.update_balance()
                    self.N_Tree += 1
                    
                # Right subtree is larger than left subtree  
                if self.balance < -1:
                    # balance > 0 need RL rotation
                    if self.root.right.balance > 0:
                        self.root.right.rotate_right()
                        self.update_height()
                        self.update_balance()
                        self.N_Tree += 1
                    # Need L rotation    
                    self.rotate_left()
                    self.update_height()
                    self.update_balance()
                    self.N_Tree += 1
                    
                    
    def rotate_left(self) -> None:
        """ Right rotation"""
        new_root = self.root.right.root                     
        new_left_sub = new_root.left.root
        old_root = self.root

        self.root = new_root
        new_root.left.root = old_root
        old_root.right.root = new_left_sub
        
            
    def rotate_right(self) -> None:
        """ Left rotation"""
        new_root = self.root.left.root
        new_left_sub = new_root.right.root
        old_root= self.root 
        
        self.root = new_root
        new_root.right.root = old_root
        old_root.left.root = new_left_sub
        
          
    def delete(self, key: int) -> None:
        """ Delete key from the tree"""
        
        if not self.root:
          raise ValueError ("The AVL tree is empty")
        
        
        elif self.root != None:
            if self.root.key == key:
                # Key found in leaf node, just erase it
                if not self.root.left.root and not self.root.right.root:
                    self.root = None
                # Node has only one subtree (right), replace root with that one    
                elif not self.root.right.root:
                    self.root = self.root.left.root
                # Node has only one subtree (left), replace root with that one    
                elif not self.root.left.root:                
                    self.root = self.root.right.root
                else:
                    # Find  successor as smallest node in right subtree
                    successor = self.root.right.root
                    while successor.left.root != None:
                        successor = successor.left.root
                    self.root.key = successor.key
                    # Delete successor from the replaced node right subree
                    self.root.right.delete(successor.key) 
            elif key < self.root.key:
                 self.root.left.delete(key)
            elif key > self.root.key:
                 self.root.right.delete(key)
            
            
        self.update_height()
        self.update_balance()
        self.control_balance()
        self.N_Tree += 1
        
         
    def printInorder(self) -> list:
        """
        Inorder traversal of the tree(Left subree + root + Right subtree)
        """ 
        result = []
 
        if not self.root:
           return result
        else:
           result.extend(self.root.left.printInorder())
           result.append(self.root.key)
           result.extend(self.root.right.printInorder())
        return result
    
    
    def display(self, root=None, level=0) -> None:
        """ Display the final tree"""
        if not root:
            root = self.root

        if root.right.root:
            self.display(root.right.root, level + 1)
            print (('\t' * level), ('    /'))

        print (('\t' * level), root)

        if root.left.root:
            print (('\t' * level), ('    \\'))
            self.display(root.left.root, level + 1)
    
            
def main() -> None:     
  tree =  AVLTree()
  data = [5,1,2,3,4,9]
  for key in data:  
     tree.insert(key)
  tree.delete(3)
  tree.delete(4)
  tree.insert(8)
  
  print(tree.printInorder())
  tree.display()
  print("The number of AVL_tree's formed is : " + str(tree.N_Tree))

if __name__ == "__main__":
    main()
    