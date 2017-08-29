"""Big-sorting
https://www.hackerrank.com/challenges/big-sorting/problem
Idea : stable sort, sort by 2 keys
"""
#!/bin/python3

import sys


n = int(input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in range(n):
   unsorted_t = str(input().strip())
   unsorted.append(unsorted_t)
# your code goes here
unsorted.sort()
sorted_ar = sorted(unsorted, key = len)
for num in sorted_ar:
    print(num)
