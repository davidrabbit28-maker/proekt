def sort_arr(arr): # arr = lst = [15, 3, 2, 8, 6] -> [2, 3, 15, 8, 6] -> [2, 3, 15, 8, 6]
    n = len(arr)
    shet = 0
    for i in range(n):
        print(f"\nШаг {i + 1}:")
        print(f"Текущее состояние {arr}:")
        min_idx = i # "15" - индекс минимального числа, 0 
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]: # 2 < 6
                min_idx = j # 2, число 2
                shet += 1
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
        
    return arr, f"Количество подмен = {shet}"





lst = [15, 3, 2, 8, 6]
print(sort_arr(lst))