import random

correct = False
com_num = random.randint(1,100)

while correct == False:
    you_num = int(input("숫자를 입력하세요(1~100) : "))
    if you_num == com_num:
        correct = True
        print("정답입니다.")
    else:
        if you_num > com_num:
            print("큽니다.");
        else:
            print("작습니다.");
