"""
Quick Sort
Time complexity better case: O(nlogn)
Time complexity worse case: O(n^2)
Depends on the selection of pivot.
It is a sorting algorithm based on divide and conquer.

Types of pivot:
First element= 0 
Middle elemenet = len(arr) // 2
Last element = len[-1]
Random pivote = ramdom selected

1.Compare the values of the list vs the pivote and divide in 3 arrays:
    less = element less than the pivote.
    middle = element equal to the pivote.
    greater = element greater than the pivote.

2.Use recursivity
    for the less array and greater array value.
    -Select a new pivote and comparate the elements of the array.

3.Return the sorted array. 
"""


def quickSort(n:list[int]):
    if len(n) <= 1:
        return n

    pivote = n[-1]
    
    less = []
    equal = []
    greater = []

    for value in n:
        if pivote > value:
            less.append(value)
        elif value == pivote:
            equal.append(value)
        else:
            greater.append(value)

    
    return quickSort(less)+equal + quickSort(greater)

if __name__ == '__main__':

    print(quickSort([9,4,1,16,1,6]))
    print(quickSort([-1,4,1,16,-12,15]))



