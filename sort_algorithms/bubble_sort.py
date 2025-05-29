"""
Bubble sort
Time complexity: O(n^2)
It is a sorting algorithm.
1.Compare the current number with the number of the right:
    Less than. Move on to next iteration.
    Greater than. The current element and swap with the element of the right.
2.At the end of the first iteration the last value will be the greatest value of the list.
    Skip the last i position because its already sorted.
3.Repeat until the list is sorted. 
"""

def bubble_sort(elements: list) -> list:

    long = len(elements)
    for i in range(long):
        for j in range(long-1-i):
            if elements[j] > elements[j+1]:
                elements[j], elements[j+1] = elements[j+1], elements[j]
    
    return elements


if __name__ == '__main__':

    print(bubble_sort([1,9,5,2,80,1]))
    print(bubble_sort([4,3,2,1,1,3]))
