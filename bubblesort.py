def bubble(lst):
      for i in range(len(lst)):
          changed = False
          for j in range(i+1,len(lst)):
              if lst[i]>lst[j]: 
                  changed = True
                  lst[i],lst[j] = lst[j],lst[i]
          if not changed: break
      return lst 

def insertion(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def merge(lst):
    left = lst[:len(lst)//2]
    right = lst[len(lst)//2:]
    if len(left) > 1: left = merge(left)
    if len(right) > 1:right = merge(right)
    ret = []
    leftc = 0
    rightc = 0
    while leftc < len(left) and rightc < len(right):
      if left[leftc] < right[rightc]:
        ret.append(left[leftc])
        leftc += 1
      else:
        ret.append(right[rightc])
        rightc += 1
    ret += left[leftc:] if leftc == len(left) else right[rightc:]
    return ret
  
def selection(array):
  n = len(array)
  for i in range(n):
      min_idx = i
      for j in range(i + 1, n):
          if array[j] < array[min_idx]:
              min_idx = j
      (array[i], array[min_idx]) = (array[min_idx], array[i])
      
import time
from datetime import timedelta
start_time = time.monotonic()
start = time.process_time()

print(merge([4,21,6,45,3,546]))
end_time = time.monotonic()
# print(timedelta(seconds=end_time - start_time))    
elapsed = (time.process_time() - start)
print(elapsed)
print(insertion([4,21,6,45,3,546])) 