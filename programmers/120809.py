# 배열 두배 만들기

# 120809

# 문제
# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 각 원소에 두배한 원소를 가진 배열을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    answer = []
    for i in numbers:
        i = int(i)*2
        answer.append(i)
        
    return answer

# ========
# 리스트 컴프리헨션 방식
# [ <출력표현식> for <변수> in <이터러블> ]
def solution(numbers):
  return [num*2 for num in numbers]

# ========
# 넘파이 활용 방식
import numpy as np
def solution(numbers):
  answer = []
  answer = np.array(numbers)*2
  answer = answer.tolist()
  return answer
