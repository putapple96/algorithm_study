time = 0

def solution(cacheSize, cities):
    cache = []
    for c in cities:
        LRU(cache, cacheSize, c.lower())
    return time


def LRU(cache, cacheSize, city):
    global time
    if cacheSize == 0:
        time += 5
        return
    if len(cache) == 0:
        time += 5
        cache.insert(0, city)
        return
    if len(cache) == cacheSize:
        if cache.count(city) == 0:
            time += 5
            cache.pop()
            cache.insert(0, city)
        elif cache.count(city) == 1:
            time += 1
            cache.remove(city)
            cache.insert(0, city)
    else:
        if cache.count(city) == 0:
            time += 5
            cache.insert(0, city)
        elif cache.count(city) == 1:
            cache.remove(city)
            time += 1
            cache.insert(0, city)
    return
        