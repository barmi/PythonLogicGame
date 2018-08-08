import random

correct = False
com_num = random.randint(1,100)

while correct == False:
    you_num = input("숫자를 입력하세요(1~100) : ")
    if you_num == com_num:
        corrrect = True
        print("정답입니다.")
