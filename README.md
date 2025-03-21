# CUATSHackathon2025

**Overview of Big-O notation**
Analysing an algorithm: predicting the resources that the algorithm requires

Time (CPU time)
Memory
Bandwidth

Best case running time-
Average case running time
worst case running time

We focus on the worst case running time as best case will be unlikely 
Blind 75
Neetcode 150

Python uses dynamic arrays natively : collection of elements stored at contiguous memory location. Efficient data retrieval and manipulation

Operation | Big-O-notation | Notes
Access    | O(1)           |Search is O(n)
Insert    | O(n)           |O(1) if appending. Need to shift everything to insert
Delete    | O(n)           |O(1) if at the end of an array

Hashmap are Dictionaries:

Hashmap = {}
Hashset = set()

What is a Hash?

A value associated to an input. Hashmaps - assign a hash value to a key and then based on the hash value the next position is determined. Collisions can happen therefore can theoretically be O(n)

Practically: Hashmaps are O(1) for for Access, Insert, Delete HOWEVER NO SENSE OF ORDER

Kadane's Algorithm

Finding the maximum sum of a contiguous subarray:
[4,-1,2,-7,3,4]

[4] Current Sum = 4 Max Sum = 4

[4,-1] Current Sum = 3 Max Sum = 4

[4,-1,2] Current Sum = 4 Max Sum = 5

[4,-1,2,-7] Current Sum = -2 Max Sum = 5

[3] Current Sum = 3 Max Sum = 5

[3,4] Current Sum = 7 Max Sum = 7

Pointers
Binary Search for a value in sorted list in O(log(n))
Left Pointer Right Pointer

Linked Lists

Access O(n)
Search O(n)
Insert O(1)
Delete O(1)


Trees

If we have a balanced tree, the search algorithm will run in O(logn) time. 

Depth First Search - GO AS DEEP AS POSSIBLE AND THEN BACKTRACK

Inorder
Left All the way Right

def inorder(root):
  if not root:
    return inorder(root.left)
  print root.val


Preorder 

Postorder

BACKTRACKING - RECURSION

Breadth First Search



def inorder_dfs(root):
    if root is None:
        return
    
    # Traverse left subtree
    inorder_dfs(root.left)
    
    # Visit current node
    print(root.value, end=' ')
    
    # Traverse right subtree
    inorder_dfs(root.right)


  Double Ended Queues 


Graphs

Most commonly graphs are represented as matrices
Graphs | Matrix DFS
Counting Paths across a matrix with obstacles









