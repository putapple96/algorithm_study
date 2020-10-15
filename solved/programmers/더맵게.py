import heapq

def solution(scoville, K):
    pq = []
    for scv in scoville:
        heapq.heappush(pq, scv)
    cnt = 0
    while pq[0] < K:
        try:
            first = heapq.heappop(pq)
            second = heapq.heappop(pq)
            heapq.heappush(pq, first + (second * 2))
            cnt += 1
        except:
            return -1
    return cnt