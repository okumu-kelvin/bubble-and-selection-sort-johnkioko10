def selection_sort(arr):
    def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    pass

my_list = [6,2,44,5,59,3,1,3]
selection_sort(my_list)
print(my_list)
    pass
