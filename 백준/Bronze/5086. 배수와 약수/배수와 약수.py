# BOJ 5086번
while True:
    x, y = map(int, input().split())
    
    if x == 0 and y == 0:
        break
    if not y % x:
        print('factor')
    elif not x % y:
        print('multiple')
    else:
        print('neither')
