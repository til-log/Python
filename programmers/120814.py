# 피자 나눠 먹기 (1)

# 120814

# 문제
# 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때, 모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

# 입출력
# n	 | result
# 7	 |  1
# 1  | 	1
# 15 |	3

def solution(n):
  # 7명 초과일 때 7을 나눠서 나머지가 1 이상이다
    if n>7 and n%7 >= 1:
      # 1을 더한 값을 출력한다.
        return (n//7)+1
  # 
    elif n>=7 and n%7==0:
        return (n//7)
    else :
        return 1

# 나머지 초점으로 생각해서 작업했음
# 다만 코드가 불필요하게 길고 중첩되는 조건이 있기 때문에
# 더 간단하게 짤 수 있는 방식 고안

def solution(n):
  if n%7 == 0:
    return (n//7)
  else:
    return (n//7)+1
    
# =======
# https://school.programmers.co.kr/learn/courses/30/lessons/120814/solution_groups?language=python3
# 다른사람들꺼 추가로 확인 필요
# 몫 초점으로 진행한게 있었음
