from collections import Counter

N = input()
n_cards = input().split()
M = input()
m_cards = input().split()

counter = Counter(n_cards)

for card in m_cards:
    result = counter[card]
    print(result, end=' ')