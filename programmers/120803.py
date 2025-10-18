# 두 수의 차 구하기

# 120803

# 문제
# 정수 num1과 num2가 주어질 때, num1에서 num2를 뺀 값을 return하도록 soltuion 함수를 완성해주세요.

# 입출력 예
# num1	num2	result
# 2  	3	-1
# 100	2	98

def solution(num1, num2):
    answer = num1 - num2
    return answer


# ========
# 120802와 같이 람다 활용 가능
solution = lambda num1, num2 : num1-num2
