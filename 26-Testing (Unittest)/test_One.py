import unittest 
import One



class TestOne(unittest.TestCase):
    def test_add(self): 
        result = One.add(10, 7)
        self.assertEqual(result, 17)
        
    def test_mul(self): 
        self.assertEqual(One.mul(5,5) , 25) 
        self.assertEqual(One.mul(2,4) , 8) 
        self.assertEqual(One.mul(-8,-2) , 16)    
    
    def test_divid(self): 
        # self.assertRaises(ValueError ,One.divid , 2,0)
        with self.assertRaises(ValueError): 
            One.divid(2,0)
        self.assertEqual(One.divid(4 , 2) ,2 )
        
    def test_init_pop(self):
        result = One.init_pop(4 , 3)
        self.assertIsNotNone(result)
        self.assertEqual(len(result) , 3)
        cells = [True if len(i)==4 else False for i in result]
        self.assertTrue(all(cells))         
        
        
if __name__ == "__main__":
    unittest.main()       