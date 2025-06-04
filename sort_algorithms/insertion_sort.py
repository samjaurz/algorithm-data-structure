"""
Insertion Sort
Time complexity: O(n^2)
It is a sorting algorithm.
1.Start from the second element.
2.Compare the value of the current element and the left of the current element:
    Less than. shift all the elements greater than current element to the right and insert in the correct position.
                all the elements in the left of the current position become sorted.
    Greater than. shift to next element because its already in the correct position.
3.Repeat until the list is sorted.
"""

def InsertSort(elements: list) -> list:

    long = len(elements)
    for i in range(1,long):
        current = elements[i]
       
        j = i -1
        while j >= 0 and elements[j] > current: #1 , 9
            elements[j+1] =elements[j] 
            j -=1
        elements[j+1] = current

    return elements

if __name__ == '__main__':

    print(InsertSort([9,4,1,16,1,15]))
    print(InsertSort([-1,4,1,16,-12,15]))

    