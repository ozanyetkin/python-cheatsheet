# %% Factorial
# 5! = 1 * 1 * 2 * 3 * 4 * 5
def factorial(n):
    if n == 0:  
        return 1 # 0! = 1
    return n * factorial(n-1)

print(factorial(5))

#%%

def n_binary(n, accumulated=''):
  if n == 0:
    return [accumulated]
  else:
    return (n_binary(n-1, accumulated+'0') +  
            n_binary(n-1, accumulated+'1')  )

print(n_binary(3))

#%%

def rvrs(s):
    # Base case
    if len(s) == 0:
        return s
    # Recursion
    return rvrs(s[1:]) + ([s[0]])

print(rvrs([1.0,3.3,4.3,2.3,2004,2,5,23]))

#%%

def linear_search(lst, target):
    for item in lst:
        if item == target:
            return True
    return False

def binary_search(lst, target):
    # Base case
    # Empty list (the target is not here)
    if len(lst) == 0:
        return False
    mid_pos = len(lst) // 2
    # We found the target
    if lst[mid_pos] == target:
        return True
    # Recursive
    if lst[mid_pos] > target:
        return binary_search(lst[0:mid_pos], target)
    else: # lst[mid] < target
        return binary_search(lst[mid_pos+1:], target)


def binary_search_2(data, target, low, high):
  if low > high:
    return False
  else:
    mid = (low + high) // 2
    if target == data[mid]:
      return mid
    elif target < data[mid]:
      return binary_search_2(data, target, low, mid-1)
    else:
      return binary_search_2(data, target, mid+1, high)


import random

test_array = sorted([ random.randint(0,1000000) for _ in range(1000000)])

import time

starttime = time.perf_counter()
linear_search(test_array, 999995)
print(f"Linear search done in {time.perf_counter() - starttime} seconds")

starttime = time.perf_counter()
binary_search(test_array, 999995)
print(f"Binary search 1 done in {time.perf_counter() - starttime} seconds")

starttime = time.perf_counter()
binary_search_2(test_array, 999995, 0, 1000000)
print(f"Binary search 2 done in {time.perf_counter() - starttime} seconds")


