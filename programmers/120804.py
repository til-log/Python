# 두 수의 곱 구하기

# 120804

# 문제
# 정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.

# 입출력 예
# num1	num2	result
# 3	     4	12
# 27	19	513


def solution(num1, num2):
    answer = num1 * num2
    return answer


# =======
# * 연산자 없이 반복 구조 덧셈으로 곱셈 제작
def solution(num1, num2):
    answer = 0
    for _ in range(num2):
        answer += num1
    return answer
