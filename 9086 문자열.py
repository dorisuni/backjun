# 문제
# 문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.

# 입력
# 입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 한 줄에 하나의 문자열이 주어진다. 문자열은 알파벳 A~Z 대문자로 이루어지며 알파벳 사이에 공백은 없으며 문자열의 길이는 1000보다 작다.

# 출력
# 각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.

#나의 풀이

# T = int(input())

# for i in range(T):
#     n=input()
#     print(n[0])
#     print(n[-1])
    

#틀렸다고 함. 인터넷 풀이는 다음과 같다

# 1. case_num 을 통해 입력 횟수를 입력 받습니다.

case_num = int(input())
 

# 2. case_num 만큼 word 를 입력 받고, word 인덱스의 0번과 맨끝(-1)번을 출력합니다.

for _ in range(case_num):
    word = input()
    print(word[0], word[-1], sep='')

# 결국 문제가 아니라 답을 보고 추론을 해야하는데, 내가 하고 있는 이 방식은 답은 보지 않고 문제만 보고 풀기 때문에
# 마지막 글자를 연속해서 뽑는게 다음줄에 뽑는 줄 알았다. 답을 보고 이렇게 하라고 추론해야 한다.
# 당연히 (print(word[0],word[-1],sep='')) 으로 했었을 것임 하지만 sep,end무슨차인지는 모르겠음.아하!

#end와 sep의 차이

# end and sep are optional parameters of Python. The end parameter basically prints after all the output objects present in one output statement have been returned. the sep parameter differentiates between the objects.

# EXAMPLE:

# a=2
# b='abc'
# print(a,b,sep=',')
# print(a,b,end=',')

# OUTPUT:

# 2,abc
# 2 abc,