# BOJ 1966번
n = int(input())

for _ in range(n):
    length, target = map(int, input().split())
    arr = [i for i in range(length)]

    weights = list(map(int, input().split()))
    comparison = sorted(weights, reverse=True)

    queue = []
    for i in comparison:
        while arr:
            if i == weights[0]:
                x = arr.pop(0)
                y = weights.pop(0)
                queue.append(x)
                break        
            else:
                x = arr.pop(0)
                y = weights.pop(0)
                arr.append(x)
                weights.append(y)
            
    print(queue.index(target) + 1)