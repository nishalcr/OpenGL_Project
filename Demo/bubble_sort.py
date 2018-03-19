def bubble_sort_function(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        for j in range( n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [10, 19, 15, 5, 1]
print("The sorted array :")
bubble_sort_function(arr)
print(arr)