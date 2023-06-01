while True:
    lines = list(map(int, input().split(' ')))
    c = max(lines)
    lines.remove(c)
    if c == 0:
        break
    elif c**2 == (lines[0])**2 + (lines[1])**2:
        print('right')
    elif c**2 != (lines[0])**2 + (lines[1])**2:
        print('wrong')