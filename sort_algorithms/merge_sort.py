"""
Merge sort
Time complexity: O(nlogn)
It is a sorting algorithm based on divide and conquer.
1.Use recursivity to divide the array to find the case base 
    find the case base of the left side
    find the case base of the right side
2.Call the funcion merge(recived two list of sorted elements) with that values and sorted the elements
    return the list
3.Recursive combines all the result and retrieve a sorted list.
"""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])      
    right_half = merge_sort(arr[mid:])     

    return merge(left_half, right_half)    

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged


if __name__ == '__main__':

    print(merge_sort([8,2,6,4,5]))
    #print(merge_sort([9,4,88,1,16,1,15]))

