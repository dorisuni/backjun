# 문제
# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 예를 들어, 서로 다른 9개의 자연수

# 3, 29, 38, 12, 57, 74, 40, 85, 61

# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.


list = []
for i in range(9):
    list.append(int(input()))
count = 0
max = max(list)    
for i in range(len(list)):
    count+=1
    if (max == list[i]):
        break
print(max)
print(count)
    


# 이런 방식도 가능하다.
#여기서 한줄로 표현한 numbers는  list comprehension으로 작성한 코드인데,

# 리스트 컴프리헨션(List Comprehension)은 파이썬에서 매우 강력하고 간결한 방법으로 리스트를 생성하는 기술입니다. 
# 리스트 컴프리헨션을 사용하면 루프를 사용하여 리스트를 채우는 번거로운 작업을 간단하게 수행할 수 있습니다.
# [표현식 for 항목 in iterable if 조건]
# 여기서 각 부분의 역할은 다음과 같습니다:
# 표현식: 리스트에 추가할 값을 나타냅니다.
# 항목: iterable(예: 리스트, 튜플, 문자열 등)의 각 요소를 반복하면서 사용됩니다.
# iterable: 반복 가능한 객체(예: 리스트, 튜플, 문자열 등)를 나타냅니다.
# 조건 (선택사항): if 키워드를 사용하여 조건을 지정하면, 조건을 만족하는 항목만 리스트에 추가됩니다.


numbers = [int(input()) for _ in range(9)]

print(max(numbers))
print(numbers.index(max(numbers)) + 1)

#1부터 10까지의 값을 짝수만 even_numbers 리스트에 넣기
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
