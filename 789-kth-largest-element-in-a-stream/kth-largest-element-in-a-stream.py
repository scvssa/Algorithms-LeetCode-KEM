
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








class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.heap = []
        self.k = k 

        for x in nums:
            bubble_up(self.heap, x)
            if len(self.heap)>k:
                pop_min(self.heap)

    def add(self, val: int) -> int:

        if len(self.heap) < self.k:
            bubble_up(self.heap, val)
        elif val > self.heap[0]:
            pop_min(self.heap)
            bubble_up(self.heap, val)

        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)