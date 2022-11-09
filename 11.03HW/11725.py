#시간초과
import sys
input = sys.stdin.readline

N = int(input()) #반복 횟수 지정
dict={} 
list=['1'] #root_node 값 미리 대입

for i in range(N-1):
    a,b=input().split() #입력 받은 값을 부모 노드와 자식 노드로 나눔
    if a in list:
        dict[b] = a #b의 부모 노드 번호 = a
        list.append(b) #입력 받은 값 중 부모 노드와 자식 노드를 구분하기 위해 list에 값 정리
    elif b in list:
        dict[a] = b #a의 부모 노드 번호 = b
        list.append(a)

for i in range(N-1): 
    print(dict[str(i+2)]) #dic[2]부터 dict[N-1]까지 순서대로 출력


