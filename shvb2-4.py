nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])
matrix = []
mxsum = 0
cords = []
for i in range(n):
    matrix.append(input().split(' '))
for x in range(n):
    for y in range(m):
        cx = x
        cy = y
        s = 0
        while cx > 0 and cy < m:
            s += int(matrix[cx][cy])
            cy += 1
            if cy >= m:
                break
            s += int(matrix[cx][cy])
            cx -= 1
            if cx < 0:
                break
            s += int(matrix[cx][cy])
            cy += 1

        if s > mxsum:
            mxsum = s
            cords = [x, y]
print(mxsum)
print(cords[0] + 1, cords[1] + 1)