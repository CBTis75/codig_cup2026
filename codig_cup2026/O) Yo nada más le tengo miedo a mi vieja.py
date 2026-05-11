import sys
input = sys.stdin.readline

n, q = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]

line = input().strip()
if line == "":
    pass
else:
    data_buffer = [line]
    def get_line():
        if data_buffer:
            return data_buffer.pop()
        return input().strip()
else_flag = False
if 'get_line' not in locals():
    get_line = lambda: input().strip()

for _ in range(q):
    line = get_line()

    while line == "":
        line = get_line()
    
    data = line.split()

    if data[0] == 'U':
        x = int(data[1]) - 1
        y = int(data[2]) - 1
        v = int(data[3])
        mat[x][y] = v

    else:  # Q
        x1 = int(data[1]) - 1
        y1 = int(data[2]) - 1
        x2 = int(data[3]) - 1
        y2 = int(data[4]) - 1

        mn = float('inf')
        mx = float('-inf')

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                val = mat[i][j]
                if val < mn:
                    mn = val
                if val > mx:
                    mx = val

        print(mx - mn)