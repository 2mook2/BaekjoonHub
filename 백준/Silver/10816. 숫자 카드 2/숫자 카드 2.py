from collections import Counter

N = int(input())
n_cards = list(map(int, input().split()))
M = int(input())
m_cards = list(map(int, input().split()))

counter = Counter(n_cards)

for card in m_cards:
    result = counter[card]
    print(result, end=' ')