def bubble_up (heap, x):
    
    heap.append (x)
    i = len (heap) - 1 

    while i > 0 :
        parent = (i - 1) // 2
        if heap[parent] <= heap[i]:
            break
        heap [parent], heap [i] = heap [i], heap [parent] 
        i = parent 


def pop_min (heap):
    root = heap [0]
    last = heap.pop()

    if heap:
        heap [0] = last 
        i = 0 
        n = len (heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i 

            if left < n and heap [left] < heap [smallest]:
                smallest = left 
            if right < n and heap [right] < heap [smallest]:
                smallest = right 

            if smallest == i:
                break

            heap [i], heap [smallest] = heap [smallest], heap [i]
            i = smallest

    return root 





class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #Считаем частоту повторений 
        freq = {}
        for x in nums:
            if x in freq:
                freq [x] += 1 
            else:
                freq [x] = 1 

        heap = []

        for num, cnt in freq.items():
            bubble_up(heap, (cnt, num))
            if len(heap) > k:
                pop_min(heap)


        ans =[]

        for cnt, num in heap:
            ans.append(num)
        
        return ans

        

