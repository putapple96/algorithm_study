t = int(input())

for tc in range(t):
    n, m = map(int, input().split())
    
    container = list((map(int, input().split())))
    truck = list((map(int, input().split())))

    sorted_truck = sorted(truck, reverse=True)
    sorted_container = sorted(container, reverse=True)
    weight_sum = 0
    
    for c in range(len(sorted_truck)):
        for w in range(len(sorted_container)):
            capacity = sorted_truck[c]
            weight = sorted_container[w]
            if capacity >= weight and weight != -1:
                weight_sum += weight
                sorted_container[w] = -1
                break
    
    print("#{} {}".format(tc+1, weight_sum))
