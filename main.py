from function.FourArithmeticOperations import *
if __name__ == "__main__":
    firstNum = input('１つ目の値を入力してください:')
    secondNum = input('２つ目の値を入力してください:')
    a = FourArithmeticOperations()
    a.add(int(firstNum), int(secondNum))