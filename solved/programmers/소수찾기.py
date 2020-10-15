from itertools import permutations
import math

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = set()
    n = len(numbers)
    candis = []
    for i in range(1,n+1):
        permu = list(set(permutations(numbers, i)))
        for p in permu:
            candis.append(''.join(p))
    for candi in candis:
        if isPrime(int(candi)):
            answer.add(int(candi))
    return len(answer)