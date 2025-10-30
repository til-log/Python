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


# 작업 완료 +


# 추가 방법 1=================
from scipy import stats

def solution(array):
    # scipy.stats의 mode 함수를 이용해 최빈값과 등장 횟수 계산
    # keepdims로 배열 형태 반환할 수 있게 명시해야 함 True 안써두면 에러 발생
    mode_result = stats.mode(array, keepdims=True)
    
    # 최빈값
    mode_value = mode_result.mode[0]
    # 최빈값 등장 횟수
    mode_count = mode_result.count[0]
    
    # 고유값 리스트 내 몇 번 등장했는가 확인
    counts = [array.count(i) for i in set(array)]
    # 전체 원소 중 가장 많이 등장한 횟수
    max_count = max(counts)
    
    # 최빈값이 여러 개라면 -1 출력
    if counts.count(max_count) >= 2:
        return -1
    else:
        return mode_value

# 추가 방법 2=================
# https://docs.python.org/ko/3/library/collections.html#collections.Counter
from collections import Counter

def solution(array):
    # 입력으로 주어진 정수 배열에서 각 원소 등장 빈도 계산
    # array 예시  [1,2,3,4,5,6,5,5,5]라면
    # Counter({5: 4, 1: 1, 2: 1, 3: 1, 4: 1, 6: 1})
    counter = Counter(array)

    # 등장 빈도가 높은 순서대로 (값, 빈도) 쌍 정렬해 상위 2개 추출
    # [(5, 4), (1, 1)]
    most_common = counter.most_common(2)

    # 최빈값이 1개만 있는 경우
    # 배열에 서로 다른 값이 하나만 존재하거나
    # 가장 많이 등장한 값의 빈도가 두 번째로 많이 등장한 값의 빈도보다 클 때
    if len(most_common) == 1 or most_common[0][1] > most_common[1][1]:
        return most_common[0][0]
    else:
        return -1
