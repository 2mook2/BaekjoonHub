# BOJ 28279번
import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())

덱 = deque()
for _ in range(n):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 1:
        덱.appendleft(cmd[1])
    
    elif cmd[0] == 2:
        덱.append(cmd[1])
    
    elif cmd[0] == 3:
        print(덱.popleft() if 덱 else -1)
    
    elif cmd[0] == 4:
        print(덱.pop() if 덱 else -1)
        
    elif cmd[0] == 5:
        print(len(덱))
        
    elif cmd[0] == 6:
        print(1 if not 덱 else 0)
        
    elif cmd[0] == 7:
        print(덱[0] if 덱 else -1)
        
    elif cmd[0] == 8:
        print(덱[-1] if 덱 else -1)