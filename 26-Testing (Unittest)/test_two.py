import unittest 
from two import Student



class TestOne(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):  # case sensative
        pass
    
    @classmethod
    def tearDownClass(cls): # case sensative
        pass
    
    def setUp(self): # case sensative
        self.std1 = Student('mahmood' , 'kherad' , 0.0)
        self.std2 = Student('ahmad' , 'rezayi' , 0.0)
    
    def tearDown(self): # case sensative
       pass   
    
    
    def test_mail(self):
        self.assertEqual(self.std1.mail() , 'mahmood.kherad@gmail.com')
        self.assertEqual(self.std2.mail() , 'ahmad.rezayi@gmail.com')             
    
    
    def test_full_name(self):
        self.assertEqual(self.std1.full_name() , 'mahmood kherad')
        self.assertEqual(self.std2.full_name() , 'ahmad rezayi') 
        
        
    def test_inc_mark(self): 
        self.std1.inc_mark() 
        self.std2.inc_mark() 
        self.std2.inc_mark()      
         
        self.assertEqual(self.std1.mark , 0.5)
        self.assertEqual(self.std2.mark , 1.0)     
            
        
        
if __name__ == "__main__":
    unittest.main()       