def selection_sort(arr):
    n = len(arr)
    
    # Проходим по каждому элементу массива
    # i — это текущая позиция, ставим на нее минимальный элемент 
    for i in range(n - 1):
        
        # Предполагаем, что минимальный элемент находится на позиции i
        min_index = i
        
        # Ищем минимальный элемент в оставшейся части массива 
        for j in range(i + 1, n):
            
            # Если нашли элемент меньше текущего минимального, то сохраняем индекс
            if arr[j] < arr[min_index]:
                min_index = j
        
        
        # меняем местами текущий элемент и найденный минимальный
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


numbers = [64, 25, 12, 22, 11]

print(selection_sort(numbers))