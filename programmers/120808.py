# 분수의 덧셈

# 120808

# 문제
# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

# 최대공약수
def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def solution(numer1, denom1, numer2, denom2):
    answer = []
    # 공통 분모
    denom = denom1*denom2
    # 교차곱 분자 계산
    numer = (numer1*denom2) + (numer2*denom1)
    
    # 최대공약수 계산
    g = gcd(numer, denom)
    # 정수 형태로 나눔
    numer //=g
    denom //=g
    
    # 저장
    answer.append(numer)
    answer.append(denom)
    return answer

# ====
# fractions 모듈 사용
from fractions import Fraction

def solution(numer1, denom1, numer2, denom2):
    answer = 0
    # Fraction 분자,분모
    answer = Fraction(numer1, denom1) + Fraction(numer2, denom2)
    return [answer.numerator, answer.denominator]
