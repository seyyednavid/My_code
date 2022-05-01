import unittest

from new_stack import stack

class TestStack(unittest.TestCase):
    
    item1 = 1
    item2 = '2'
    item3 = [3]
    item4 = 'navid'
    
    def test_push(self):
        stk = stack()
        stk.push(self.item1)
        stk.push(self.item2)
        stk.push(self.item3)
        stk.push(self.item4)
        
        self.assertEqual(stk.size, 4)
        self.assertRaises(ValueError, stk.push, None)
        
        stk.push(self.item1)
        stk.push(self.item2)
        stk.push(self.item3)
        stk.push(self.item4)
        stk.push(self.item1)
        stk.push(self.item1)  #stack is full
        
        self.assertRaises(MemoryError, stk.push, self.item3)
        

    
    def test_pop(self):
        stk=stack()
        stk.push(self.item1)
        stk.push(self.item2)
        stk.push(self.item3)
            
            
        self.assertEqual(stk.pop(), self.item3)
        self.assertEqual(stk.size, 2)
        
        self.assertEqual(stk.pop(), self.item2)
        self.assertEqual(stk.size, 1)
        
        self.assertEqual(stk.pop(), self.item1)
        self.assertEqual(stk.size, 0)
        
        self.assertEqual(stk.pop(), None)
        self.assertEqual(stk.size, 0)
            
            
            
if __name__=='__main__':
    unittest.main()            
            
            
            
            
        
        
        
        
    
        
    
        

