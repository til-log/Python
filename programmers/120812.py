# 최빈값 구하기

# 120812

# 문제
# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

def solution(array):
    # 입력값 정렬
    x = sorted(array)
    # 입력값 정렬+중복 제거 -> 고유값
    check = sorted(list(set(x)))

    # 고유값 등장 횟수 저장 리스트
    counts = []

    # 고유값 개수당 반복
    for i in check:
        # 원래 리스트에서 고유값 원소에 대해 빈도 계산 및 저장
        counts.append(x.count(i))

    # 최빈값 빈도 계산
    max_count = max(counts)

    # 최빈값 개수가 2개 이상일 경우 -1값 리턴
    if counts.count(max_count) >= 2:
        return -1

    # 최빈값이 유일한 경우
    else :
        # 인덱스 구해서 해당 인덱스값으로 출력
        max_index = counts.index(max_count)
        return check[max_index]

  # ======
from scipy import stats
# 해당 방식으로도 작업할 수 있도록 작성해둘 예정 
# 및 다른 방식 확인 필요
# https://school.programmers.co.kr/learn/courses/30/lessons/120812/solution_groups?language=python3

