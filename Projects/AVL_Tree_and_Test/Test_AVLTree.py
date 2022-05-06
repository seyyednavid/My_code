# Test AVL_Tree

import unittest
from My_AVL_Tree import AVLNode
from My_AVL_Tree import AVLTree



class TESTAVLTree(unittest.TestCase):
    
    
    def test_AVLnode_init(self):
        """ Test __init__ for AVL_node class"""
        n = AVLNode(5)
        self.assertEqual(n.key, 5)
        self.assertEqual(n.left, None)
        self.assertEqual(n.right, None)
###############################################################################        
            
    def test_AVLTree_init(self):
        """ Test __init__ for AVL_Tree class"""
        t = AVLTree()
        self.assertEqual(t.root, None)
        self.assertEqual(t.height, 0)
        self.assertEqual(t.balance, 0)
        
###############################################################################
        
    def test_AVLTree_insert_with_one_node(self):
        """ Insert root in avl tree"""
        t = AVLTree()
        t.insert(5)
        self.assertEqual(t.root.key, 5)
        self.assertEqual(t.height, 1)
        self.assertEqual(t.balance, 0)
        self.assertEqual(t.N_Tree, 1)
        
        
    def test_AVLTree_insert_leftside_root(self):
        """ Insert in left side of avl tree"""
        t = AVLTree()
        t.insert(5)
        t.insert(1)
        self.assertEqual(t.root.key, 5)
        self.assertEqual(t.height, 2)
        self.assertEqual(t.balance, 1)
        # there is a node in the left side of root
        self.assertEqual(t.root.left.height, 1)
        self.assertEqual(t.root.left.balance, 0)
        self.assertEqual(t.root.right.height, 0)
        self.assertEqual(t.root.right.balance, 0)
        self.assertEqual(t.N_Tree, 2)
        
        
    def test_AVLTree_insert_rightside_root(self):
        """ Insert in right side of avl tree"""
        t = AVLTree()
        t.insert(5)
        t.insert(7)
        self.assertEqual(t.root.key, 5)
        self.assertEqual(t.height, 2)
        self.assertEqual(t.balance, -1)
        self.assertEqual(t.root.left.height, 0)
        self.assertEqual(t.root.left.balance, 0)
        # there is a node in the right side of root
        self.assertEqual(t.root.right.height, 1)
        self.assertEqual(t.root.right.balance, 0)
        self.assertEqual(t.N_Tree, 2)
        
###############################################################################
        
    def test_AVLTree_right_rotate(self):
        """ Right rotation"""
        t = AVLTree()
        t.insert(5)
        t.insert(4)
        t.insert(3)
        # Root five had height=3 and balance=2, so we had to use rotation. 
        # because self.root.left.height = +1, we just need right_rotate
        self.assertEqual(t.root.key, 4)
        self.assertEqual(t.height, 2)
        self.assertEqual(t.balance, 0)
        self.assertEqual(t.N_Tree, 4)
        
        
    def test_AVLTree_left_rotate(self):
        """ left rotation"""
        t = AVLTree()
        t.insert(5)
        t.insert(7)
        t.insert(9)
        # Root five had height=3 and balance= -2, so we had to use rotation. 
        # because self.root.left.height = -1, we just need right_rotate
        self.assertEqual(t.root.key, 7)
        self.assertEqual(t.height, 2)
        self.assertEqual(t.balance, 0)
        self.assertEqual(t.N_Tree, 4)
        
          
    def test_AVLTree_insert_LR_rotate(self):
        """ left right rotation"""
        t = AVLTree()
        t.insert(5)
        t.insert(1)
        t.insert(2)
        # Root=five had balance=2.because self.root.left.balance < 0, so we 
        #had to use left and then right rotate. therefore 2 became new root to
        #retain the balance
        self.assertEqual(t.root.key, 2)
        self.assertEqual(t.height, 2)
        self.assertEqual(t.balance, 0)
        self.assertEqual(t.N_Tree, 5)

###############################################################################

    
    def test_AVLTree_delete_empty_tree(self):
            # Delete empty tree
            with self.assertRaises(ValueError) as ex:
              t = AVLTree()
              t.delete(5)
              self.assertEqual(str(ex.exception),"The AVL tree is empty")
            
           
    def test_AVLTree_delete_with_one_node(self):
            """ Delete root from the tree"""
            t = AVLTree()
            t.insert(5)
            t.delete(5)
            # root will be deleted.
            self.assertEqual(t.root, None )
            self.assertEqual(t.height, 0 )
            self.assertEqual(t.balance, 0)
            
            
    def test_AVLTree_delete_root_WithRightTree(self):
            """ Delete root. when it has right tree and has not left tree"""
            t = AVLTree()
            t.insert(5)
            t.insert(7)
            t.delete(5)
            self.assertEqual(t.root.key, 7 )
            self.assertEqual(t.height, 1 )
            self.assertEqual(t.balance, 0)
            
            
    def test_AVLTree_delete_root_WithLeftTree(self):
            """ Delete root. when it has left tree and has not right tree"""
            t = AVLTree()
            t.insert(5)
            t.insert(2)
            t.delete(5)
            self.assertEqual(t.root.key, 2 )
            self.assertEqual(t.height, 1 )
            self.assertEqual(t.balance, 0)
            
            
    def test_AVLTree_delete_root_WithLeftRightTree(self):
            """ Delete root. when it has both left and right tree"""
            t = AVLTree()
            t.insert(5)
            t.insert(2)
            t.insert(7)
            t.delete(5)
            self.assertEqual(t.root.key, 7 )
            self.assertEqual(t.height, 2 )
            self.assertEqual(t.balance, 1)
            
    
    def test_AVLTree_delete_root_by_successor(self):
            """
            Delete root. when it has both left and right tree and right tree.
            moreover root's right tree has left tree and we must use successor.
            """
            t = AVLTree()
            t.insert(5)
            t.insert(2)                     
            t.insert(7)
            t.insert(6)
            t.delete(5)
            self.assertEqual(t.root.key, 6 )
            self.assertEqual(t.height, 2 )
            self.assertEqual(t.balance, 0)
            
     

if __name__ == "__main__":
    unittest.main()
    