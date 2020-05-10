# import 修正しました :Pro-doct
from function import fourArithmeticOperations
if __name__ == "__main__":
    # 関数に渡すときに変換するのも汚いと思ったので修正いたしました
    # また機能実装の追加があれば、ここをどうするか話し合いましょう     :Pro-doct
    # 入力をfloatにして、割り算追加してみました　:uji
    while True:
        print("=" * 40)
        menu = input("Top画面\n 0:終了 1:まとめて四則演算 2:式入力")

        if menu == "0":
            break
        elif menu == "1":
            firstNum = float(input('１つ目の値を入力してください:'))
            secondNum = float(input('２つ目の値を入力してください:'))
            a = fourArithmeticOperations.FourArithmeticOperations()
            a.add(firstNum, secondNum)
            a.sub(firstNum, secondNum)
            a.mult(firstNum, secondNum)
            a.div(firstNum, secondNum)
        elif menu == "2":
            result = input('計算式を入れてください')
            print(eval(result))
        else:
            print("指定された数字を選択してください")
