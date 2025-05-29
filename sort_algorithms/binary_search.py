
"""
Binary search
Time complexity: O(log N)
The list must be sorted.
It is and algorithm for search based on divide and conquer.
1.Divide the list and retrieve the middle number
    -Calculate with inferior limit + superior limit and divide by 2
2.Compara if its the target and if is, return True
3.Its evaluate the the result with the target.
    -Less than < ajust the supeior limit and get the middle number
    -Greater than > ajust the inferior limit and get the middle number
4.Repeat until fiend the target is found.If not in the list return False
"""

def binary_search(nums:list, target):
    
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = (low + high) // 2

        if nums[middle] == target:
            return True
        elif nums[middle] < target:
            
            low = middle + 1
        elif nums[middle] > target:
            high = middle - 1

    return False

if __name__ == '__main__':

    print(binary_search([-15,1,2,3,4,5],-15))
    print(binary_search([0,1,2,3,4,5],-12))
    print(binary_search([0,1,2,3,4,5],9))
    print(binary_search([2, 5, 8, 12, 16, 23, 38, 56, 72, 91],23))




