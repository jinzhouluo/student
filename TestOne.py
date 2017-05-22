from ParametrizedTestCase   import ParametrizedTestCase  
import unittest
import thread

class TestOne(ParametrizedTestCase):  
    def test_something(self):  
        print 'param =', self.param  
        print 'params =', self.params
        self.assertEqual(1, 1)  

    def test_something_else(self):  
        self.assertEqual(2, 2)  


fruits = [42, 13]
for fruit in fruits:
    suite = unittest.TestSuite()
    suite.addTest(ParametrizedTestCase.parametrize(TestOne, param=fruit,params=fruit))  
    
    thread.start_new_thread( unittest.TextTestRunner(verbosity=2).run(suite), ("Thread-1", 2, ) )