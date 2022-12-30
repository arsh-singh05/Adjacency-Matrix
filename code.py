# Python program to display subtree of nodes
# Implementing adjacency matrix

from collections import defaultdict 
# to make use of adjacency matrix 
def convert(a): 
	adjList = defaultdict(list) 
	for i in range(len(a)): 
		for j in range(len(a[i])): 
					if a[i][j]== 1: 
						adjList[i].append(j) 
	return adjList 

# driver code 
    #       Node0                   Node1                Node2                   Node3
a =[[0,1,1,1,0,0,0,0,0,0], [1,0,0,0,1,0,0,0,0,0], [1,0,0,0,0,1,1,0,0,0], [1,0,0,0,0,0,0,1,0,0],
    #       Node4                   Node5                Node6                   Node7
    [0,1,0,0,0,0,0,0,0,0], [0,0,1,0,0,0,0,0,0,0], [0,0,1,0,0,0,0,0,0,0], [0,0,0,1,0,0,0,0,1,1],
    #       Node8                   Node9
    [0,0,0,0,0,0,0,1,0,0], [0,0,0,0,0,0,0,1,0,0]] # adjacency matrix 
AdjList = convert(a) 

#To print subtree of all nodes  
  
# arrays for keeping the position at  
# each dfs traversal for each node  
start = [None] * 100001 
endd = [None] * 100001
  
# To store dfs order  
dfs_order = []  
adj = [[] for i in range(100001)]  
visited = [False] * 100001
  
# Recursive function for dfs traversal dfsUtil()  
def dfs(a, b):  
   
    # To keep track of the nodes visited  
    visited[a] = 1 
    b += 1
    start[a] = b  
    dfs_order.append(a)  
      
    for it in adj[a]:  
        if not visited[it]:  
            b = dfs(it, b)  
       
    endd[a] = b 
    return b 
   
# Function to print the subtree nodes  
def Print(n):  
   
    for i in range(0, n):  
       
        # To check if node is leaf node  
        # start[i] is equals to end[i]  
        if start[i] != endd[i]:  
           
            print("subtree of node", i, "is", end = " ")  
            for j in range(start[i]+1, endd[i]+1):  
               
                print(dfs_order[j-1], end = " ")  
               
            print() 

#*
def rec(i, parent, height):
	if (parent[i] == -1):
		return 1
		
	if (height[i] != -1):
		return height[i]

	height[i] = rec(parent[i], parent, height) + 1

	return height[i]

def findHeight(parent, n):
	res = 0
	height = [-1]*(n)

	for i in range(n):
		res = max(res, rec(i, parent, height))

	return res
 #*           
# Driver code  
if _name_ == "_main_":  
    # No of nodes n = 10  
    n, c = 10, 0 
    adj[0].append(1)  
    adj[0].append(2)  
    adj[0].append(3)  
    adj[1].append(0)  
    adj[1].append(4)  
    adj[2].append(0)  
    adj[2].append(5)  
    adj[2].append(6)
    adj[3].append(0)
    adj[3].append(7)
    adj[4].append(1)
    adj[5].append(2)
    adj[6].append(2)
    adj[7].append(3)
    adj[7].append(8)
    adj[7].append(9)
    adj[8].append(7)
    adj[9].append(7)
    # adj[0].append(1)
    # adj[0].append(2)
    # adj[1].append(3)
    # adj[1].append(4)
    # adj[1].append(0)
    # adj[2].append(5)
    # adj[2].append(6)
    # adj[2].append(0)
    # adj[3].append(1)
    # adj[4].append(1)
    # adj[5].append(2)
    # adj[6].append(2)
    # adj[5].append(7)
    # adj[7].append(5)
    # Calling dfs for node 0  
    # Considering root node at 0  
    dfs(0, c)  
    # Print child nodes  
    Print(n)
    parent=[-1,0,0,0,1,2,2,3,7,7]
    #parent=[-1,0,0,1,1,2,2,5]
    l=int(len(parent))
    height = findHeight(parent, l)
    print("Height of the given tree is: ",height)
