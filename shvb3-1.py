def get(cell):
    global tab
    j = 0
    if cell[0] == 'B':
        j = 1
    if cell[0] == 'C':
        j = 2
    if cell[0] == 'D':
        j = 3
    if cell[0] == 'E':
        j = 4
    i = int(cell[1])
    return tab[i][j]


expr = input()
tab = []
for s in range(5):
    tab.append(list(map(int, input().split(' '))))
calc = []
while len(expr) > 2:
    calc.append(expr[:2:])
    calc.append(expr[2])
    expr = expr[3::]
calc.append(expr)
while '*' in calc:
    i = calc.index('*')
    a = calc[i - 1]
    if isinstance(calc[i - 1], str):
        a = get(calc[i - 1])
    b = calc[i + 1]
    if isinstance(calc[i + 1], str):
        b = get(calc[i + 1])
    calc = calc[:i - 1:] + [a * b] + calc[i + 2::]
while len(calc) > 1:
    a = calc[0]
    if isinstance(calc[0], str):
        a = get(calc[0])
    b = calc[2]
    if isinstance(calc[2], str):
        b = get(calc[2])
    if calc[1] == '+':
        calc = [a + b] + calc[3::]
    else:
        calc = [a - b] + calc[3::]
print(calc[0])
