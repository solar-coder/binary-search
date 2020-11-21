# Author: SolarCoder
# Instagram | @solarcoder

# binary search accepting the target, array, start index, end index
def binary_search(n, arr, start, end):

    # calculating wwhat the middle index is.
    middle_index = (start + end)// 2

    # if the middle element is the number,
    # we found it
    if arr[middle_index] == n:
        return middle_index
    
    # if the middle element is greater than the number,
    # we search in the left half of the array next
    elif arr[middle_index] > n:
        return binary_search(n, arr, start, middle_index-1)
    
    # if the midle element is less than the number,
    # we search in the right half of the array next
    elif arr[middle_index] < n:
        return binary_search(n, arr, middle_index+1, end)

# initializing array
array = [0, 1,2, 3, 5, 6]

# searching for 6 within the array, starting at index 0, and ending at the last index
print(binary_search(6, array, 0, len(array)))

# Output: 5