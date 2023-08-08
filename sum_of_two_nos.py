# for sorted array
# def sum(arr, target_num):
#     n = len(arr)
#     pairs = []
#     for i in range(n - 1):
#         for j in range(i + 1, n):
#             if arr[i] + arr[j] == target_num :
#                 pairs.append([i,j])
#     return pairs


# arr = [2, 4, 10, 12, 22]
# target_num = 14
# indices = sum(arr, target_num)
# print(indices)


# def sum(arr, target_num):
#     n = len(arr)
#     pairs = []
#     left = 0
#     right = n - 1

#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == target_num:
#             pairs.append([left, right])
#             left += 1
#             right -= 1
#         elif current_sum < target_num:
#             left += 1
#         else:
#             right -= 1

#     return pairs

# arr = [2, 4, 10, 12, 22]
# target_num = 14
# indices = sum(arr, target_num)
# print(indices)



# for unsorted array
# def sum(arr, target_num):
#     n = len(arr)
#     arr.sort()  

#     pairs = []
#     left = 0
#     right = n - 1

#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == target_num:
#             pairs.append([left, right])
#             left += 1
#             right -= 1
#         elif current_sum < target_num:
#             left += 1
#         else:
#             right -= 1

#     return pairs

# arr = [2, 22, 12, 4, 10]
# target_num = 14
# indices = sum(arr, target_num)
# print(indices)

#using tim sort 

# Timsort implementation

# def insertion(arr, left, right):
#     for i in range(left + 1, right + 1):
#         key = arr[i]
#         j = i - 1
#         while j >= left and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# def merge(arr, left, mid, right):
#     len1 = mid - left + 1
#     len2 = right - mid
#     left_arr = arr[left:mid+1]
#     right_arr = arr[mid+1:right+1]

#     i = j = 0
#     k = left

#     while i < len1 and j < len2:
#         if left_arr[i] <= right_arr[j]:
#             arr[k] = left_arr[i]
#             i += 1
#         else:
#             arr[k] = right_arr[j]
#             j += 1
#         k += 1

#     while i < len1:
#         arr[k] = left_arr[i]
#         i += 1
#         k += 1

#     while j < len2:
#         arr[k] = right_arr[j]
#         j += 1
#         k += 1

# def tim_sort(arr):
#     n = len(arr)
#     min_run = 32

#     for i in range(0, n, min_run):
#         insertion(arr, i, min(i + min_run - 1, n - 1))

#     size = min_run
#     while size < n:
#         for start in range(0, n, size * 2):
#             mid = min(start + size - 1, n - 1)
#             end = min(start + 2 * size - 1, n - 1)
#             merge(arr, start, mid, end)
#         size *= 2

#     return arr


# def sum(arr, target_num):
#     n = len(arr)
#     arr = tim_sort(arr) 

#     pairs = []
#     left = 0
#     right = n - 1

#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == target_num:
#             pairs.append([left, right])
#             left += 1
#             right -= 1
#         elif current_sum < target_num:
#             left += 1
#         else:
#             right -= 1

#     return pairs

# arr = [2, 22, 12, 4, 10]
# target_num = 14
# indices = sum(arr, target_num)
# print(indices)


#binary search implementation


def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def sum(arr, target_num):
    n = len(arr)
    arr.sort()  

    pairs = []

    for i in range(n - 1):
        complement = target_num - arr[i]
        index = binary_search(arr, i + 1, n - 1, complement)
        if index != -1:
            pairs.append([i, index])

    return pairs

arr = [2, 22, 12, 4, 10]
target_num = 14
indices = sum(arr, target_num)
print(indices)
