#틀렸습니다
#반례를 못 찾겠습니다 ㅠㅠ
import sys
input = sys.stdin.readline

a, b, c, m = map(int,input().split())

tired = 0
work = 0
for i in range(0,25):
    if m-tired < a: #쉼
        tired = tired-c
        if tired < 0:
            tired = 0
    else : #일
        tired = tired + a
        work = work + b
print(work)