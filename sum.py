def sum_array(arr, index):
    if index < 0:
        return 0
    
    return arr[index] + sum_array(arr, index - 1)

arr = [12, 22, 30, 1, 50, 6]
sum = sum_array(arr, len(arr) - 1)
print("Sum:", sum)
