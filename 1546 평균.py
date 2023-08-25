# 문제
# 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 
# 이 값을 M이라고 한다. 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.

# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.

# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 
# 둘째 줄에 세준이의 현재 성적이 주어진다. 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 
# 적어도 하나의 값은 0보다 크다.

# 출력
# 첫째 줄에 새로운 평균을 출력한다. 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.

#세준이는 자기점수중에서 최댓값을 골랐다.

# N = int(input())

#내가 푼 풀이
N = 4
scores = list(map(int,input().split()))
print(scores)
scores1 = [20, 40, 60, 80]


total = 0
total1 = 0
for i in scores1:
    total1+=i
Max = max(scores)

scores2 = [x/Max*100 for x in scores1]
print(scores2)
for i in scores2:
    total+=i
print(total1/len(scores1))
print(total/len(scores2))

#즉 식을 정리하면,


N = int(input())
scores = list(map(int,input().split()))
total = 0
Max =max(scores)
scores2 = [x/Max*100 for x in scores]
for i in scores2:
    total+=i
print(total/N)

