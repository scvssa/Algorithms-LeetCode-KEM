class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len (nums) <= 1: 
            return nums
        
        mid = len (nums) // 2

        # рекурсивно сортируем правую и левую части 
        left = self.sortArray (nums[:mid])
        right = self.sortArray (nums[mid:])

        #объединяем отсортированные половины
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:

        # массив в который кладем результат сортировки
        result = [] 

        # указатели для левой и правой части массива 
        i = 0
        j = 0 

        # сравниваем элементы двух массивов 
        while i < len (left) and j < len (right):
            if left[i] < right[j]:
                
                # если левый элемент меньше, то добавляем его в массив и сдвигаем указатель 
                result.append(left[i])
                i += 1
            else:

                # если правый элемент меньше, то добавляем его в массив и сдвигаем указатель 
                result.append(right[j])
                j += 1 

        # если в одном из массивов остались элементы, то добавляем их в конец результата
        result.extend(left[i:])
        result.extend(right[j:])

        # возвращаем объедененный массив 
        return result
    