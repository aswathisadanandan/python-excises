def diagonal_difference(matrix):
    l = sum(matrix[i][i] for i in range(N))
    r = sum(matrix[i][N-i-1] for i in range(N))
    return abs(l - r)

matrix = []
N = input()
for _ in range(N):
    matrix.append(map(int, raw_input().split()))
diagonal_difference(matrix)
