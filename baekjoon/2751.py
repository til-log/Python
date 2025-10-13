# 수 정렬하기 2

# 2751

# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# 예제 입력
# 5
# 5
# 4
# 3
# 2
# 1

# 예제 출력
# 1
# 2
# 3
# 4
# 5

# 병합정렬


# N = int(input().strip())
# num_input = []
# for i in range(N):
#     val = int(input().strip())
#     num_input.append(val)

import sys
# 지역 바인딩으로 반복 호출 때 속도를 올림
# 루프 내 다중 호출 시 속성 조회 비용 절감시켜 미세 성능 향상을 노림
read = sys.stdin.readline

# 첫 입력으로 개행 제거 및 int 변환하여 몇 번을 입력할지 확인
N = int(read().strip())
# N개의 정수를 각 줄에서 하나씩 읽어 리스트로 구성
num_input = [int(read().strip()) for _ in range(N)]


# 병합 정렬 함수. 해당 리스트를 받아 정렬된 새 리스트 반환
# 왼쪽 절반과 오른쪽 절반을 각각 정렬
# 두 정렬 리스트를 병합해서 전체도 정렬할 예정
def divide_and_conquer_and_combine(x):
    # 길이가 0이거나 1일 경우엔 정렬 완료된 상태이기에 곧바로 return
    if len(x) <= 1:
        return x
    
    # Divide
    # 리스트의 반절은 어디부터인지 확인
    mid = len(x) // 2
    # Conquer
    # 해당 인덱스 기준으로 리스트를 반절씩 나눔
    # 재귀 호출로 계속해서 작게 쪼개감
    left = divide_and_conquer_and_combine(x[:mid])
    right = divide_and_conquer_and_combine(x[mid:])

    # Combine
    # 두 정렬된 리스트를 하나의 정렬 리스트로 병합할 예정
    # 인덱스 위치 포인터 재설정. 반복문이 돌 때마다 1씩 증가하면서 리스트의 끝으로 이동할 예정
    l = r = 0
    # 최종 결과가 저장될 리스트
    lr = []

    # 두 리스트 모두에 원소가 남아있는 동안 지속해서 비교
    while l < len(left) and r < len(right):
        # 같은 값일 때 왼쪽 원소가 먼저 들어가도록
        if left[l] <= right[r]:
            # 더 작거나 같은 값을 결과에 저장
            lr.append(left[l])
            # 왼쪽 포인터 추가
            l+=1
        else:
            # 오른쪽 값이 더 작은 경우이기에 결과에 추가
            lr.append(right[r])
            # 오른쪽 포인터 추가
            r+=1

    # 루프 종료. 둘 중 하나 끝을 도달해 비교할 값이 없기 때문에 통째로 붙임
    lr.extend(left[l:])
    lr.extend(right[r:])

    # 병합 완료된 정렬 리스트 반환
    return lr

# 정렬 실행
res = divide_and_conquer_and_combine(num_input)

# 출력
print('\n'.join(map(str, res)))
