# 문제
# 단어 
# $S$와 정수 
# $i$가 주어졌을 때, 
# $S$의 
# $i$번째 글자를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 영어 소문자와 대문자로만 이루어진 단어 
# $S$가 주어진다. 단어의 길이는 최대 
# $1\,000$이다.

# 둘째 줄에 정수 
# $i$가 주어진다. (
# $1 \le i \le \left|S\right|$)

# 출력
#  
# $S$의 
# $i$번째 글자를 출력한다.

#나의 풀이
 
word = input()
N = int(input())
print(word[N-1])

#리스트의 첫번째 인덱스는 0이라는 사실을 기억하자.

