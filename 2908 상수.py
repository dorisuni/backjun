# 문제
# 상근이의 동생 상수는 수학을 정말 못한다. 
# 상수는 숫자를 읽는데 문제가 있다. 이렇게 수학을 못하는 상수를 위해서 상근이는 수의 크기를 비교하는 문제를 내주었다. 
# 상근이는 세 자리 수 두 개를 칠판에 써주었다. 그 다음에 크기가 큰 수를 말해보라고 했다.

# 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 
# 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.

# 두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 상근이가 칠판에 적은 두 수 A와 B가 주어진다. 두 수는 같지 않은 세 자리 수이며, 0이 포함되어 있지 않다.

# 출력
# 첫째 줄에 상수의 대답을 출력한다.

#나의 풀이

N,M = map(str,input().split())

reversed_N = ""
reversed_M = ""
for i in N:
   reversed_N = i+reversed_N
   
for j in M:
    reversed_M = j+reversed_M
    
num1 = int(reversed_M)
num2 = int(reversed_N)
if num1>num2:
    print(num1)
else:
    print(num2)

#구글검색한 쉽게 푸는방법

num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순으로뒤집기
num2 = int(num2[::-1])
print(num1) if num1 > num2 else print(num2)
