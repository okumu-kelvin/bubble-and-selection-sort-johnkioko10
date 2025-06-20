def bubble_sort(unsorted_list):
    def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if unsorted_list[j] > unsorted_list[j + 1]:
                unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]
    pass

my_list = [6,2,44,5,59,3,1,3]
bubble_sort(my_list)
print(my_list)
    pass
