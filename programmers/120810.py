# 나머지 구하기

# 120810

# 문제 설명
# 정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.

# 입출력 예
# num1	num2	result
# 3	2	1
# 10	5	0

# 파이썬
# / 실수 나눗셈
# // 정수 나눗셈 => 소수점 이하 버린 몫
# % 나머지 연산


def solution(num1, num2):
    answer = num1 % num2
    return answer


# ======
# 120804와 같이 다른 시각으로 살펴봄<- 곱셈을 더하기 반복구조로 계산 추가함
# 나눗셈도 반복적인 뺄셈이므로...
def solution(num1, num2):
    while num1 >= num2:
        num1-=num2
    return num1
# ex)14,3
# 14->11
# 11->8
# 8->5
# 5->2
# num1=2 형태


