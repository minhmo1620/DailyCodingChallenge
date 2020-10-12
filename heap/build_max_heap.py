"""
There are three ways to build a heap in Python
- manually build
- use PriorityQueue
- use Heapq
"""

# Case 1: Using Heapq
import heapq

class Node:
    def __init__(self, val):
        self.val = val
    
    def __lt__(self, other):
        return self.val > other.val

def calculate_product(heap):
    if len(heap) < 3:
        return -1
    return heap[0].val * heap[1].val * heap[2].val

def add_one_element(heap, val):
    heapq.heappush(heap, val)
    return calculate_product(heap)

A = [1, 2, 3, 4, 5]
h = []
for i in (A):
    print(add_one_element(h, Node(i)))

# Case 2: Using Priority Queue
import queue

class Node:
    def __init__(self, val):
        self.val = val
    
    def __lt__(self, other):
        return self.val > other.val

def calculate_product(pq):
    if len(pq.queue) < 3:
        return -1
    return pq.queue[0].val * pq.queue[1].val * pq.queue[2].val 

def add_one_element(pq, val):
    pq.put(val)
    
    return calculate_product(pq)

A = [1, 2, 3, 4, 5]
pq = queue.PriorityQueue()

for i in (A):
    print(add_one_element(pq, Node(i)))

# Case 3: Build max_heap manually
def build_max_heap(h):
    n = len(h)
    for i in range (n//2 - 1, -1, -1):
        maxHeapify(i)

def maxHeapify(i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < len(h) and h[left] > h[largest]:
        largest = left 
    
    if right < len(h) and h[right] > h[largest]:
        largest = right
    
    if i != largest:
        h[i], h[largest] = h[largest], h[i]
        maxHeapify(largest)

def calculate_product(h):
    if len(h) < 3:
        return -1
    p = 1
    tmp = []
    for _ in range(3):
        p *= h[0]
        tmp.append(h[0])
        pop_first_element(h)
    
    for i in tmp:
        add_one_element(h, i)
    
    return p

def pop_first_element(h):
    n = len(h)
    
    if n == 0:
        return 
    
    h[0] = h[n-1]
    h.pop()
    maxHeapify(0)


def add_one_element(h, val):
    h.append(val)
    i = len(h) - 1
    
    while i != 0 and h[(i - 1)//2] < h[i]:
        h[i], h[(i - 1)//2] = h[(i - 1)// 2], h[i]
        i = (i - 1)//2
 
A = [1, 2, 3, 4, 5]
h = []
for i in (A):
    add_one_element(h, i)
    print(calculate_product(h))
