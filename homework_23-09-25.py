# 1.
# b**2 - 4*a*c формула
def num_of_solution(a,b,c) -> int:
    if b**2 < 4*a*c:
        return 0
    elif b**2 == 4*a*c:
        return 1
    else:
        return 2
# sol = num_of_solution(-100,0,1)
# print(f'Equation have {sol} solution')

# 2.
s = input('>>>')
def valid(s: str) -> bool:
    if s == '':
        return False
    vd = ('(','[','{')
    zd = (')',']','}')
    # Це створює словник відповідних дужок
    # ключі - відкриваючі, значення - закриваючі
    # d_map - Відровідність дужок
    d_map = dict(zip(vd,zd))
    stack = []
    if s[0] in zd:
        return False
    for i in s:
        if i in vd:
            stack.append(i)
        elif i in zd:
            top = stack.pop()
            if d_map[top] != i:
                return False
    return True
print(valid(s))