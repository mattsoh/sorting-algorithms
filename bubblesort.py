import random
import time

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
  
def selection(lst):
  n = len(lst)
  for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        (lst[i], lst[min_idx]) = (lst[min_idx], lst[i])
      
def radix(lst):
    maxx = max(lst)
    exp = 1
    while maxx // exp > 0:
        buckets = [[] for _ in range(10)]
        ret = []
        for i in lst:
            buckets[i//exp%10].append(i)
        for i in buckets:
            for j in i:
                ret.append(j)
        lst = ret[:]
        exp += 1
    return lst




def quick(lst, left = None, right = None):
    if left == None: left = 0
    if right == None: right = len(lst)
    if right-left < 1:
        return lst
    pivotloc = random.randint(left, right)
    pivot = lst.pop(pivotloc)
    pointer = left
    while pointer <= right-1:
        print(pointer, pivot)
        if lst[pointer] > pivot and pivotloc > pointer:
            lst.insert(right-1,lst.pop(pointer))
            pivotloc -= 1
        elif lst[pointer] < pivot and pivotloc <= pointer:
            lst.insert(left,lst.pop(pointer))
            pointer += 1
            pivotloc += 1
        else:
            pointer += 1
    lst.insert(pivotloc,pivot)
    quick(left,pivotloc)
    quick(pivotloc+1, right)
    return lst
# quick(0,len(lst)-1)
# print(lst)

print("Which sorting algorithm would you like?")
print("")
option = input("Input: ")
start = time.process_time()
res = eval(option)([4,21,6,45,3,546])
print(time.process_time() - start)
print(res)