import heapq

q = int(input())

count_map = {}   
heap = []       
total = 0        
for _ in range(q):
    query = input().split()
    t = int(query[0])

    if t == 1:
        x = int(query[1])

        if x not in count_map:
            count_map[x] = 1
            heapq.heappush(heap, x)
        else:
            count_map[x] += 1

        total += 1

    elif t == 2:
        h = int(query[1])

        while heap and heap[0] <= h:
            x = heapq.heappop(heap)

            if x in count_map:
                total -= count_map[x]
                del count_map[x]

    print(total)