#[50 pts] Write a program that takes a value “n” as input; produces “n” random numbers 
# with a uniform distribution between 1 and n and places them in a linked list in sorted order. 
# Place each one individually in the linked list where they belong to be in order, 
# do not sort the list after placing them there.

import random 
import time 
import matplotlib.pyplot as plt 

#linked list code got from https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm

class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

ll = SLinkedList()

nums = []
runtimes = []

while True: 
    q = input("continue?:")
    if q != "":
        break 
    n = input("enter a number:" ) 
    start = time.time()
    for x in range(0,int(n)): 
        num = random.randint(1,int(n))
        #print(num)
        if ll.headval is None: 
            ll.headval = Node(num)
        else: 
            cur = ll.headval 
            prev = ll.headval 
            while cur: 
                if num < cur.dataval: 
                    break 
                else: 
                    prev = cur 
                    cur = cur.nextval 
            
            if cur is None: 
                prev.nextval = Node(num)
            elif cur == ll.headval: 
                ll.headval = Node(num)
                ll.headval.nextval = cur 
            else: 
                prev.nextval = Node(num)
                prev.nextval.nextval = cur 

    end = time.time()
    nums.append(n)
    runtimes.append(end-start)

plt.title("problem 2")
plt.plot(nums,runtimes)
plt.table(rowLabels = ["n", "runtime"], cellText = [nums,runtimes])
plt.tick_params(axis='x', pad=20)
plt.savefig("CS5350p2.png")
