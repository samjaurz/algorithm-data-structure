"""
-Bubble sort is algorithms of ordenamiento.
-Orden the numbers from smallest to biggest or biggest to smallest
-Recibe un arreglo de n cantidad de elementos el cual tiene un tiempo de ejecucion n(o^2)
-Hace la comparacion de elementos basado en indice
-Al recorrrer el arreglo si la comparacion es verdadera intercambiar la posicion de interacion
 element[j] por la posicion de la iteracion mas 1 element[j+1].
-Al final de la primera iteracion el ultimo valor puesto en el array sera el mayor o el menor dependiendo de el caso.
"""

def bubble_sort(element: list) -> list:

    long = len(element)
    for i in range(long):
        for j in range(long-1-i):
            # sort smallest to biggest >, sort biggest to smallest <
            if element[j] > element[j+1]:
                element[j], element[j+1] = element[j+1], element[j]
    
    return element



if __name__ == '__main__':

    print(bubble_sort([1,2,5,2,80,1]))
    print(bubble_sort([4,3,2,1,1,3]))
