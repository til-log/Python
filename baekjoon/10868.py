# 최솟값

# 10868

# 문제
# N(1 ≤ N ≤ 100,000)개의 정수들이 있을 때, a번째 정수부터 b번째 정수까지 중에서 제일 작은 정수를 찾는 것은 어려운 일이 아니다. 하지만 이와 같은 a, b의 쌍이 M(1 ≤ M ≤ 100,000)개 주어졌을 때는 어려운 문제가 된다. 이 문제를 해결해 보자.
#여기서 a번째라는 것은 입력되는 순서로 a번째라는 이야기이다. 예를 들어 a=1, b=3이라면 입력된 순서대로 1번, 2번, 3번 정수 중에서 최솟값을 찾아야 한다. 각각의 정수들은 1이상 1,000,000,000이하의 값을 갖는다.


# 입력
# 첫째 줄에 N, M이 주어진다. 다음 N개의 줄에는 N개의 정수가 주어진다. 다음 M개의 줄에는 a, b의 쌍이 주어진다.

# 출력
# M개의 줄에 입력받은 순서대로 각 a, b에 대한 답을 출력한다.

# 예제 입력
# 10 4
# 75
# 30
# 100
# 38
# 50
# 51
# 52
# 20
# 81
# 5
# 1 10
# 3 5
# 6 9
# 8 10

# 예제 출력
# 5
# 38
# 20
# 5

# =====시간 초과로 재진행======
# import sys
# read = sys.stdin.readline
# N, M = map(int, read().split())

# data = []
# for _ in range(N):
#     val = int(read().strip())
#     data.append(val)

# queries_index = []
# min_result = []
# queries_index = []
# for _ in range(M):
#     a, b = map(int, read().split())
#     queries_index.append((a, b))

#     mincase = min(data[a:b])
#     min_result.append(mincase)


# for i in min_result:
#     print(i)



# 재작성 진행===================
import sys
# 지역 바인딩으로 반복 호출 때 속도를 올림
read = sys.stdin.readline

# 입력
# N = 배열 길이, M = 쿼리 개수
N, M = map(int, read().split())
# N줄에서 값을 하나씩 읽어서 원본 배열 리스트로 제작
original = [int(read()) for _ in range(N)]

# 거듭제곱 구간을 저장할 때 N을 덮기 위해 필요한 최대 지수이기 때문에 작업 진행
# bit_length : 정수 나타내는 데 필요한 비트 수 반환 메서드
K = N.bit_length()

# 스파스 테이블 2차원 배열
# twotable[k][i] = 시작 i에서 길이 2^k 구간의 최솟값을 저장함
twotable = [[0] * N for _ in range(K)]
# 레벨 0은 원소 자체이기에 그대로 원본 나오게
twotable[0] = original[:]

# 긴 구간(2^k)의 최솟값을 채우는 루프
for k in range(1, K):

    # 2^(k-1). 길이 2^k 구간의 앞/뒤 반쪽 길이
    half = 1 << (k - 1)

    # 이번 레벨의 전체 구간 길이 2^k
    length = 1 << k

    # 시작 인덱스 i의 유효 개수
    # 구간이 배열을 넘지 않으려면 i<=N-length
    upto = N - length + 1

    # 아래 레벨(길이 2^(k-1))값을 읽어와 현재 레벨(길이 2^k)을 채우기 위함
    prev = twotable[k - 1]
    curr = twotable[k]

    # 시작 인덱스 i를 0부터 유효 범위까지 순회하며 테이블을 채움
    for i in range(upto):
        # 앞 절반의 최소 prev[i]
        # 뒤 절반의 최소 prev[i+half]
        # 길이 2^k 구간의 최소가 curr
        curr[i] = min(prev[i], prev[i + half])

# 구간 쿼리 함수 시작
def processing(L, R):
    # 질의 구간 길이 계산
    length = R - L
    # 정수 연산으로 floor(log2(length)) 구함
    k = length.bit_length() - 1
    # 2의 거듭제곱(사용할 블록) 길이 2^k
    block_len = 1 << k
    # 왼쪽 블록 최소
    left_min = twotable[k][L]
    # 오른쪽 블록 최소
    right_min = twotable[k][R - block_len]
    # 겹쳐도 전체 커버 가능하게
    # 두 값의 최솟값이 곧 구간 전체의 최솟값
    return left_min if left_min < right_min else right_min

# 결과 리스트
output = []
# 질의 순서대로 처리할 수 있도록 반복
for _ in range(M):
    # 질의 순서 입력
    # 최솟값, 최대값이지만 파이썬 인덱스를 고려하지 않고 1부터 시작하는 형태임
    a, b = map(int, read().split())
    # 최솟값의 경우 파이썬 인덱스(기존0시작)를 고려해 -1가 필요하지만
    # 최대값에는 -1값하지 않겠음(최대값을 호출할 때 매번 +1가 필요하기 때문에 불필요한 과정으로 생각)
    # b는 그대로    # R = b
    # 정리 : 단일 원소 a,b값을 받을 때 3,3이라면 내부는 2,3이 되는 형태로 길이가 1개임
    a -= 1

    # 구간 쿼리 함수 실행 결과값 리스트에 저장
    output.append(str(processing(a, b)))

# 최종 결과 호출
print("\n".join(output))
