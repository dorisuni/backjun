# 문제
# 동혁이는 오래된 창고를 뒤지다가 낡은 체스판과 피스를 발견했다.

# 체스판의 먼지를 털어내고 걸레로 닦으니 그럭저럭 쓸만한 체스판이 되었다. 하지만, 검정색 피스는 모두 있었으나, 흰색 피스는 개수가 올바르지 않았다.

# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.

# 동혁이가 발견한 흰색 피스의 개수가 주어졌을 때, 몇 개를 더하거나 빼야 올바른 세트가 되는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 동혁이가 찾은 흰색 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수가 주어진다. 이 값은 0보다 크거나 같고 10보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 입력에서 주어진 순서대로 몇 개의 피스를 더하거나 빼야 되는지를 출력한다. 
# 만약 수가 양수라면 동혁이는 그 개수 만큼 피스를 더해야 하는 것이고, 음수라면 제거해야 하는 것이다.

#내가 푼 풀이

# white = list(map(int,input().split()))
# right_piece = [1,1,2,2,2,8]
# export_value = []

# for r_idx,j in enumerate(white):
#     if(j > right_piece[r_idx]):
#         answer = right_piece[r_idx] - j
#         export_value.append(answer)
#     elif(j< right_piece[r_idx]):
#         answer = j-right_piece[r_idx]
#         export_value.append(answer)
#     else:
#         export_value.append(j)
# print(export_value) 


  

white = list(map(int,input().split()))
right_piece = [1,1,2,2,2,8]
export_value = []

for r_idx,j in enumerate(white):
    if(j > right_piece[r_idx]):
        answer = right_piece[r_idx] - j
        export_value.append(answer)
    elif(j < right_piece[r_idx]):
        answer = right_piece[r_idx] - j
        export_value.append(answer)
    else:
        export_value.append(j)

for i in range(6):
    print(export_value[i],end=' ')     


#구글링 답안
# chess = [1,1,2,2,2,8]
# a = list(map(int,input().split()))

# for i in range(6):
#     print(chess[i]-a[i],end=' ')
 
#enumerate(iterable, startIndex)

# Enumerate()에는 두가지 매개변수가 있습니다.

# Iterable : 반복할 수 있는 개체입니다.
# StartIndex : (선택 사항) 개수는 루프의 첫 번째 항목에 대해 startIndex에 제공된 값으로 시작하고 루프의 끝에 도달할 때까지 다음 항목에 대해 증가합니다.
# 지정하지 않으면 카운트는 0부터 시작 됩니다.
# 반환값:
# 입력으로 제공된 반복기(Iterable) 개체에 대한 각 항목에 대한 카운트 값과 함께 반복(Iterable) 가능한 개체를 반환합니다.