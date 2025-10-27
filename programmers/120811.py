# 중앙값 구하기

# 120811

# 문제
# 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다. 예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다. 정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    # array는 리스트이므로 iterable한 형태. 즉 sorted로 정렬 가능함
    # 정렬된 리스트를 answer에 담아둠
    answer = sorted(array)
    # 입력 array의 길이는 홀수이므로 몫 연산으로 중앙값 인덱스 구함
    x = len(answer) // 2
    # 해당 리스트에서 출력될 수 있도록
    return answer[x]
