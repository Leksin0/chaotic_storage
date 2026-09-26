size = int(input())
matrix = []
for j in range(size):
    matrix.append([])
    for q in input().split(' '):
        matrix[j].append(int(q))
diags = []

for x in range(2, size):
    cy = 0
    cx = x
    dia = []
    td = True
    while cx != 0:
        dia.append(matrix[cx][cy])
        cx -= 1
        cy += 1
    dia.append(matrix[cx][cy])
    cd = sorted(dia)
    mul = cd[1] / cd[0]
    for d in range(1, len(cd)):
        if cd[d] != cd[d - 1] * mul:
            td = False
    if td:
        diags.append(dia)

for y in range(1, size - 2):
    cx = size - 1
    cy = y
    dia = []
    td = True
    while cy != size - 1:
        dia.append(matrix[cx][cy])
        cx -= 1
        cy += 1
    dia.append(matrix[cx][cy])
    cd = sorted(dia)
    mul = cd[1] / cd[0]
    for d in range(1, len(cd)):
        if cd[d] != cd[d - 1] * mul:
            td = False
    if td:
        diags.append(dia)

if diags != []:
    print("Yes")
    for e in diags:
        for a in e:
            print(a, end=" ")
        print()
else:
    print("No")
