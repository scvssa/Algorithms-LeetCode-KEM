import random

def quick_sort (A, p, r):
    if p < r:

        q = partition(A, p, r)
        quick_sort (A, p, q-1)
        quick_sort (A, q+1, r)

    return A

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
