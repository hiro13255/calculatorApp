'''
クラス名:fourArithmeticOperations
引数: 1つ目の値
引数2：２つ目の値
'''
class FourArithmeticOperations():
    '''
    機能名：足し算
    引数1：1つ目の値
    引数2：２つ目の値
    戻り値：入力２つの値を足した結果
    作成者:ひろ　　　
    '''
    def add(self,x,y):
        result = x + y
        print(result)
        return result
    
    '''
    機能名:引き算
    引数1：1つ目の値
    引数2：２つ目の値
    戻り値：入力２つの値を引いた結果
    作成者:Pro-doct
    '''
    def sub(self, x, y):
        result = x - y
        print(result)
        return result

    '''
    機能名:掛け算
    引数1：1つ目の値
    引数2：２つ目の値
    戻り値：入力２つの値を掛けた結果
    作成者:Pro-doct
    '''
    def mult(self, x, y):
        result = x * y
        print(result)
        return result
        
    '''
    機能名:割り算
    引数1：1つ目の値
    引数2：２つ目の値
    戻り値：入力２つの値を割った結果
    作成者:uji
    '''
    def div(self, x, y):
        if y == 0:
            print("division by zero !")
            return
        result = x / y     # intで返すか、floatで返すか話し合いましょう :Pro-doct
        print(result)
        return result