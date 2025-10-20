# 숫자 비교하기

# 120807

# 문제
# 정수 num1과 num2가 매개변수로 주어집니다. 두 수가 같으면 1 다르면 -1을 retrun하도록 solution 함수를 완성해주세요.


def solution(num1, num2):
    if num1 == num2 :
        return 1
    else :
        return -1

# =======
def solution(num1, num2):
    return 1 if num1 == num2 else -1
# 형태도 가능함. if문 전체를 표현식 형태로 줄인 것
# 가독성과 직관성을 동시에 확복함
