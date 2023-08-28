# 문제
# 아래 예제와 같이 고양이를 출력하시오.

# 입력
# 없음.

# 출력
# 고양이를 출력한다.

# \    /\
#  )  ( ')
# (  /  )
#  \(__)|

#나의 풀이
#그냥 print문에 복붙하려고 하니 문자열 리터럴이 종료되지 않았다고 한다.
# print(("\    /\"))

# 그래서 입력받는 첫줄을 공백도 리스트에 포함하여 리스트를 for문을 돌려 sep('')를 껴서 출력해보려고 함.

# word = list(map(input().split()))
# print(word)

# for i in range(word):
#     print(i,sep='')
    
# 이렇게 했더니 TypeError: map() must have at least two arguments.
# 이렇게 나옴. 이건 map함수에 첫번쨰 인자를 집어넣지 않아서 그랬던 거임.

# word = list(map(str,input().split()))
# print(word)
# 이거 출력결과가 ['\\', '/\\']이렇게 나와버림.

#다음 풀이는 그냥 인풋값 출력해보기
# word = input()
# print(word)
# 아 이건 안되는게 입력값이 없음. 무조건 출력값을 출력해야함..

# 단순하게 백슬래시 두개 써보기

print("\\     /\\")
print("\\    /\\")
# 이건 된다. 백슬래시를 출력할때는 무조건 \\ 두개를 써야한다.

print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")