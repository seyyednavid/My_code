import unittest
from merge_sort_2 import merge_list

class Testmergeclass(unittest.TestCase):
    
    
    
    def test_merge_list(self):
        
        list1 = [1,5,3,6,4,9,0,7]
        list2=[1,3,6,4,8,'c']
        
        result = merge_list(list1)
        
        self.assertEqual(result[0], 0)
        self.assertEqual(result[1], 1)
        self.assertEqual(result[2], 3)
        self.assertEqual(result[3], 4)
        self.assertEqual(result[4], 5)
        self.assertEqual(result[5], 6)
        self.assertEqual(result[6], 7)
        self.assertEqual(result[7], 9)
        
        
        
        self.assertRaises(ValueError, merge_list, list2)
        
        



if __name__=='__main__':
    unittest.main() 