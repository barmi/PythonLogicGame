'''
    숫자야구게임 - 컴퓨터가 사람이 생각한 숫자를 맞추는 버전
    skshin@hs.ac.kr
    2018-08-10
'''
import random

def get_ball_count(numstr1, numstr2):
    strike = ball = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if numstr1[i] == numstr2[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    
    return strike, ball

def is_valid_num(num):
    numstr = str(num).zfill(3)
    return is_valid_numstr(numstr)

def is_valid_numstr(numstr):
    return ((numstr[0] != numstr[1]) and (numstr[0] != numstr[2]) and (numstr[1] != numstr[2]))

def input_ball_count():
    return [int(x) for x in input("볼카운트를 입력하세요(스트라크 볼) ").split()]

# ==============================================================================
# check table 관련함수
def init_check_table():
    table = [False] * 1000
    # table에서 중복되는 숫자가 있는 값을 제외한다.
    for num in range(0, 1000):
        table[num] = is_valid_num(num)
    return table

def find_valid_num_in_table(table):
    while True:
        num = random.randint(1, 999)
        if table[num]:
            return num

def update_check_table(table, check_numstr, strike, ball):
    for num in range(0, 1000):
        if table[num]:
            numstr = str(num).zfill(3)
            s,b = get_ball_count(numstr, check_numstr)
            if s != strike or b != ball:
                table[num] = False
# ==============================================================================

def game_start():
    check_table = init_check_table()
    try_count = 1

    while True:
        guess_num = find_valid_num_in_table(check_table)
        guess_numstr = str(guess_num).zfill(3)
        print(try_count, ": (", check_table.count(True), ")", guess_numstr, end = " ")
        s, b = input_ball_count()

        if s == 3:
            print(try_count, "번만에 맞췄네요.")
            break
        if s == -1 and b == -1:
            for num in range(0, 1000):
                if check_table[num]:
                    print(str(num).zfill(3))
        else:
            update_check_table(check_table, guess_numstr, s, b)
            try_count += 1
            if check_table.count(True) == 0:
                print("잘못 입력하셨네요.")
                break

game_start()
