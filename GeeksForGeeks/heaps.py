import heapq

H = []
# Create the heap

heapq.heapify(H)
print(H)

# Replace an element
heapq.heappush(H,6)
print(H)
print(type(H))

