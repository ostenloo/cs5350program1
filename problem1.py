#[50 pts] Write a program that takes a value “n” as input and prints “Hello, World” n times.

import time 
import matplotlib.pyplot as plt 

nums = []
runtimes = []

while True:  
    q = input("continue?:")
    if q != "": 
        break 
    n = input("enter a number:" ) 
    
    start = time.time()

    for x in range(0,int(n)): 
        print("Hello, World")

    end = time.time()

    nums.append(int(n))
    runtimes.append(end-start) 

plt.title("problem 1")
plt.plot(nums,runtimes)
plt.table(rowLabels = ["n", "runtime"], cellText = [nums,runtimes])
plt.tick_params(axis='x', pad=20)
plt.savefig("CS5350p1.png")
