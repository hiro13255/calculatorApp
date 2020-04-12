import unittest
import sys
sys.path.append('../')
from function.FourArithmeticOperations import *

class BasicFunctionTest(unittest.TestCase):
    '''
        足し算機能　単体テスト
    '''
    def test_add(self):
        self.assertEqual(10, FourArithmeticOperations().add(6, 4))

if __name__ == "__main__":
    unittest.main()


