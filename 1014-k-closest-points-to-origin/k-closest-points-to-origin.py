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
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        
        heap = [] 
    
        for x, y  in points:
            dist = x * x + y * y 
            bubble_up(heap, (dist, x,y))
            if len(heap)>k:
                pop_max(heap)
        

        result = []

        for dist, x, y in heap: 
            result.append([x,y])

        return result
    
    
        
    
         

    

