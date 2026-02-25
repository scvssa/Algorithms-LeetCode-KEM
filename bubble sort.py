def bubble_sort(arr):
   
    n = len(arr)
    
    # через n-1 раз массив уже будет отсортирован 
    for i in range(n - 1):
        swapped = False  # предполагаем что массив уже отсортирован 
        
    
        for j in range(n - 1 - i): # с каждой интерацией наибольший элемент "всплывает на свою позицию"
            
            # Если текущий элемент больше следующего — меняем местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        #если за интерацию не было ни одной перестановки значит массив уже отсортирован. 
        if not swapped:
            break
    
    return arr


numbers = [4, 3, 8, 2, 6, 10]

print(bubble_sort(numbers))