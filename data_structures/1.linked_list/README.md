
# Linked List

It is a data structure characterized by having nodes.  
each of which contains data and a pointer that references the next node.  


## Types of linked list 
- 1Single Linked List  
- Doubly Linked List  
- Circular Linked List  

## Common operations
- Insertion
- Deletion
- Traversal 
- Searching
- Updating



### Single Linked List
Traversal movement is only allowed,    
from the head [Fisrt node] to the tail [Last node = None]
**Nodo**: [ Data | Next pointer ]    
[1 | next ] ⇒ [2 | next  ] ⇒ ... ⇒ Null  

Code
---
```python
Class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

## Doubly Linked List


