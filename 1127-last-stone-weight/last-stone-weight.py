def bubble_up (heap, x):
    
    heap.append (x)
    i = len (heap) - 1 

    while i > 0 :
        parent = (i - 1) // 2
        if heap[parent] >= heap[i]:
            break
        heap [parent], heap [i] = heap [i], heap [parent] 
        i = parent 


def pop_max (heap):
    root = heap [0]
    last = heap.pop()

    if heap:
        heap [0] = last 
        i = 0 
        n = len (heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i 

            if left < n and heap [left] > heap [largest]:
                largest = left 
            if right < n and heap [right] > heap [largest]:
                largest = right 

            if largest == i:
                break

            heap [i], heap [largest] = heap [largest], heap [i]
            i = largest

    return root 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            bubble_up(heap, stone)
            
        while len(heap) > 1:
            a = pop_max(heap)
            b = pop_max(heap)

            if a != b: 
                bubble_up(heap, a-b)
            
        if heap:
            return heap[0]
        else:
            return 0 


