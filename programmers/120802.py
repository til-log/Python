# 두 수의 합 구하기

# 120802

# 문제
# 정수 num1과 num2가 주어질 때, num1과 num2의 합을 return하도록 soltuion 함수를 완성해주세요.

# 입출력 예
# num1	num2	result
# 2	 3	5
# 100	2	102

def solution(num1, num2):
    answer = num1 + num2
    return answer


# ------
# 가변인자와 람다 방식으로도 가능
def solution(*x):
    return sum(x)
# *args 활용으로 가변 인자를 잡아 num1, num2를 전부 포함(인자 개수 안정함을 제시)
# solution = lambda *x : sum(x)
# 으로 인자 여러 개 받는 것을 나타낼 수 있음
