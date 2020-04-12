import unittest
from function.FourArithmeticOperations import *

class BasicFunctionTest():
    '''
        足し算機能　単体テスト
    '''
    def test_add(self):
        value1 = 5
        value2 = 6
        expected = 11
        result = FourArithmeticOperations().add(value1,value2)
        self.asserrtEqual(expected,result)


unittest.main()


