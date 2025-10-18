# 몫 구하기 

# 120805

# 문제
# 정수 num1, num2가 매개변수로 주어질 때, num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.

# 입출력 예
# num1	num2	result
# 10	5	2
# 7 	2	3

# 몫이라서 //
# 나머지는 %
# 일반적 나눗셈은 /

# 기본
def solution(num1, num2):
    answer = num1//num2
    return answer


# 뺄셈으로 진행
def solution(num1, num2):
    # 몫
    i = 0
    # num1이 num2보다 커질 때 종료
    while num1>=num2:
        # tip. 최종 num2가 나머지가 됨
        num1-=num2
        i += 1
    return i

# =========================
# 내부 연산자 메서드 활용
# | 연산자    | 내부 메서드         | 예시                           |
# | -------- | ------------------- | ----------------------------- |
# | `a + b`  | `a.__add__(b)`      | `int.__add__(2, 3)` → 5       |
# | `a - b`  | `a.__sub__(b)`      | `int.__sub__(10, 4)` → 6      |
# | `a * b`  | `a.__mul__(b)`      | `int.__mul__(3, 5)` → 15      |
# | `a / b`  | `a.__truediv__(b)`  | `int.__truediv__(5, 2)` → 2.5 |
# | `a // b` | `a.__floordiv__(b)` | `int.__floordiv__(7, 3)` → 2  |
# | `a % b`  | `a.__mod__(b)`      | `int.__mod__(7, 3)` → 1       |
# 자세한건 파이썬 튜토리얼
# https://docs.python.org/3/reference/datamodel.html#special-method-names

solution = int.__floordiv__
