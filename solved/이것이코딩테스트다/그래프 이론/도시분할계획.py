# 백준 1647번
# 최소 스패닝 트리 문제인데, 두 개의 최소 스패닝 트라를 만들어야 하므로,
# MST를 구한 뒤, 가장 비용이 큰 간선을 삭제하면 될 것
import sys
input=sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a > b:
        parent[a] = b
    else:
        parent[b] = a


n , m = map(int, input().split()) # n : 집 개수(노드), m은 길의 개수(간선)

e = [] # 간선 정보 저장
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    e.append((cost, a, b)) # 비용 순으로 정렬 용이한 tuple 형태로 저장

e.sort()
ret = 0
max_cost = 0 # MST의 간선들 중 가장 큰 비용
# 아래 반복문에 따라 MST마지막에 추가되는 간선이 max_cost값이 될 것
for edge in e:
    cost, a, b= edge
    if find(parent, a) != find(parent, b): # cycle이 만들어지지 않는 경우에 대해
        union(parent, a, b)
        ret += cost
        max_cost = cost


print(ret - max_cost)

