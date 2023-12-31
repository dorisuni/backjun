# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 
# 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

#내가 푼 코드

R,S = map(str,input().split())
P = ""
for i in S:
    for _ in range(int(R)):
        P+=i
print(P)


#여기서 출력값은 맞는데 런타임 오류가 나온다.
#그래서 풀이를 검색함
#풀이는 이렇다는데

n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end='')  # end='' 옆으로 붙임
    print()  # 줄넘김
    
#그래서 이방식으로 변경해서 제출해보겟음
# 아 첫째줄에 테스트 케이스 갯수를 출력 안해서 이렇게 된거임.

T = int(input())
for _ in range(T):
    R,S = map(str,input().split())
    P = ""
    for i in S:
        for _ in range(int(R)):
            P+=i
    print(P)
    
# 이러면 된다.

