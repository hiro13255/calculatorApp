import unittest
import sys
sys.path.append('../')
# fourArithmeticOperations.py のimport を追加しました 編集者:Pro-doct
from function import fourArithmeticOperations

class BasicFunctionTest(unittest.TestCase):
    '''
        足し算機能　単体テスト
    '''
    def test_add(self):
        self.assertEqual(10, fourArithmeticOperations.FourArithmeticOperations().add(6, 4))
    '''
        引き算機能　単体テスト
        作成者:Pro-doct
    '''
    def test_sub(self):
        self.assertEqual(2, fourArithmeticOperations.FourArithmeticOperations().sub(6,4))
    
    '''
        掛け算機能　単体テスト
        作成者:Pro-doct
    '''
    def test_mult(self):
        self.assertEqual(24, fourArithmeticOperations.FourArithmeticOperations().mult(6,4))
    



if __name__ == "__main__":
    unittest.main()


