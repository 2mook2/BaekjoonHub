import sys
input = sys.stdin.readline

N = int(input())

arr = []

for i in range(N):
    command = input().split()
    
    if command[0] == 'push':
        arr.append(command[1])
        
    elif command[0] == 'pop':
        if arr:
            pp = arr.pop(0)
            print(pp)
        else:
            print(-1)
            
    elif command[0] == 'size':
        print(len(arr))
        
    elif command[0] == 'empty':
        print(int(len(arr)==0))
        
    elif command[0] == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
            
    elif command[0] == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)