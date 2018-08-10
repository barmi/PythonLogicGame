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
