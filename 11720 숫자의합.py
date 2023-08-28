# 문제
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

# 출력
# 입력으로 주어진 숫자 N개의 합을 출력한다.

#나의 풀이

N = int(input())
num = input()
total = 0

for i in range(len(num)):
    total+=int(num[i-1])
    
print(total)

#여기서 중요한 점.

# input은 str로 입력을 받는데 그냥 len(num)할 경우, 즉 for문에서 range를 설정해주지 않는 경우
# for i in 5 이런식으로 되기 때문에, int숫자는 뒤에 TypeError: 'int' object is not iterable 이런식의 타입에러를 뿜는다.