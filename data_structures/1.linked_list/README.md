
# Linked List

It is a data structure characterized by having nodes.  
each of which contains data and a pointer that references the next node.  


## Types of linked list 
- Single linked list  
- Doubly linked list  
- Circular linked list  

## Common operations
- Insertion
- Deletion
- Searching
- Updating



### Single linked list
Traversal movement is only allowed,    
from the head [Fisrt node] to the tail [Last node = None]
**Nodo**: [ Data | Next pointer ]    
[1 | next ] ⇒ [2 | next  ] ⇒ ... ⇒ None

Code
---
```python
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
```
## Doubly linked list
Traversal movement allowed in both directions  
from the head [Fisrt node] to the tail [Last node = None] and backward.  
**Nodo**: [ Previous pointer | Data | Next pointer ]    
None ⇐ [ prev | 1 | next ] ⇐⇒ [ prev | 2 | next ] ⇐⇒ [ prev| 3| next ] ⇐⇒ ..... None

Code  
---  
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```
## Circular linked list
Travesarl movemenet goes in circular
The tail [Last node] points back to the head [First node]
**Nodo** : [1 | next ] ⇒ [2 | next ] ⇒ [3 | next ] ⇒ head

Code  
---  
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```