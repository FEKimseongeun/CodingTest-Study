import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
DP = [[0]*(N+1) for _ in range(N+1)]
for _ in range(N):
    arr.append(list(map(int,input().split())))
#행
for i in range(1,N+1):
    for j in range(1, N+1):
        DP[i][j] = DP[i][j-1]+arr[i-1][j-1]
#열
for j in range(1, N+1):
    for i in range(1, N+1):
        DP[i][j] = DP[i-1][j]+DP[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1 = x1-1, y1-1
    print(DP[x2][y2]-DP[x1][y2]-DP[x2][y1]+DP[x1][y1])

