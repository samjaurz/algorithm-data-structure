"""
Insert Sort es un algoritmo de ordenamiento 
Recibe un arreglo de elementos el cual al ordenar tiene un tiempo de ejecucion n(o^2)

"""

def InsertSort(nums: list) -> list:

    for i in range(1,len(nums)):
        for j in range(i,0,-1):
            if nums[j]< nums[j-1]:
                nums[j-1], nums[j] = nums[j], nums[j-1]
            
    return nums

print(InsertSort([9,4,88,1,16,1,15]))