'''
    숫자야구게임

    각자 3자리의 숫자를 임의로 정한 뒤, 서로에게 3자리의 숫자를 불러서 결과를 확인한다.
    그리고 그 결과를 토대로 상대가 적은 숫자를 예상한 뒤 맞힌다.

    * 사용되는 숫자는 0에서 9까지 서로 다른 숫자이다.
    * 숫자는 맞지만 위치가 틀렸을 때는 볼.
    * 숫자와 위치가 전부 맞으면 스트라이크.
    * 숫자와 위치가 전부 틀리면 아웃. "틀렸다"는 게 중요하다.
    * 물론 무엇이 볼이고 스트라이크인지는 알려주지 않는다.

    출처 : https://namu.wiki/w/숫자야구
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

'''
get_ball_count() 함수 테스트
print(get_ball_count("123", "123"))
print(get_ball_count("456", "467"))
print(get_ball_count("789", "978"))
'''

def generate_three_number():
    is_done = False
    while not is_done:
        num = str(random.randint(1, 999)).zfill(3)
        if num[0] != num[1] and num[0] != num[2] and num[1] != num[2]:
            is_done = True
    return num

print(generate_three_number())
print(generate_three_number())
print(generate_three_number())
