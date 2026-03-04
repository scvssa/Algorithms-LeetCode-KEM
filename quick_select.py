import random

def quick_select(A, p, r, k):
    if p == r:
        return A[p]

    q = partition(A, p, r)
    left_size = q - p + 1

    if k == left_size:
        return A[q]
    elif k < left_size:
        return quick_select(A, p, q - 1, k)
    else:
        return quick_select(A, q + 1, r, k - left_size)

def partition (A, p, r):

    rand = random.randint(p, r)   # случайный индекс
    A[rand], A[r] = A[r], A[rand] # делаем его pivot

    x = A[r]
    i = p - 1 
    j = p 

    for j in range (p, r):

        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

nums = [2, 8, 7, 1, 3, 5, 6, 4]
k = 3
print(quick_select(nums, 0, len(nums) - 1, k))