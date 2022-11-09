import sys
input = sys.stdin.readline

def find_gcd(a,b):#최소공약수 정의
    a_division = []
    for i in range(int(a/2)):
        if a%(i+1) == 0:
            print(i+1)
            a_division.append(i+1)
            a_division.append(int(a/(i+1)))

    for i in a_division:
        if b%i == 0:
            i = i*i
    print(i)
    for i in a_division:
        

def find_lcm(a,b):

a, b = map(int,input().split())
find_gcd(a,b)
find_lcm(a,b)

#def find_lcm(a,b):
