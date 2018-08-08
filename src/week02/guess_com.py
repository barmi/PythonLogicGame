import random

correct = False
try_count = 1
# 1~100사이의 숫자
upper_num = 1
lower_num = 100

while correct == False:
    com_num = random.randint(upper_num, lower_num)
    print("숫자", com_num, "이 맞습니까?")
    choice = input("맞으면:y, 크면:b, 작으면:s 를 입력해 주세요.")
    if choice == 'y':
        correct = True
        print(try_count, "번만에 맞췄습니다.")
    try_count += 1
