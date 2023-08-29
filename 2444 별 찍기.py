# 문제
# 예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

# 출력
# 첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

# 예시

#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

#내가 푼 풀이
# N = int(input())
# list = []
# for i in range(1,N*2,2):
#     list.append("*"*i)
# for i in range(N*2,1,-2):
#     list.append("*"*i)

# for i in range(len(list)):
#     print(list[i])

#결괏값
# *
# ***
# *****
# *******
# *********
# **********
# ********
# ******
# ****
# **
#틀렸음

#구글링답
n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))
    
#나는 공백을 일단 무시했고,
#식을 제대로 구현하지 못했다.    
