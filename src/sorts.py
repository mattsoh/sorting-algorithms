import random
import time


def getTime(option, lst):
    start = time.process_time()
    print(option)
    res = algs[option](lst)
    return (time.process_time()) - start, res

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
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst
    
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
    if right == None: right = len(lst)-1
    if left >= right:
        return
    pivot_index = random.randint(left, right)
    pivot = lst[pivot_index]
    i = left
    j = right
    while i <= j:
        while lst[i] < pivot:
            i += 1
        while lst[j] > pivot:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
    quick(lst, left, j)
    quick(lst, i, right)
    return lst

def tree(lst):
    def heapify(i,n):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if left<n and lst[left]>lst[largest]:
            largest = left
        if right<n and lst[right]>lst[largest]:
            largest = right
        if largest!=i:
            lst[i],lst[largest] = lst[largest],lst[i]
            heapify(largest,n)
    n = len(lst)
    for i in range(n//2-1,-1,-1):
        heapify(i,n)
    for i in range(n-1,0,-1):
        lst[0],lst[i]=lst[i],lst[0]
        heapify(0,i)
    return lst

def bogo(lst):
    def isSorted(lst):
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                return False
        return True
    while not isSorted(lst):
        random.shuffle(lst)
    return lst

def slow(lst, left = None, right = None):
    if left == None: left = 0
    if right == None: right = len(lst)-1
    if left >= right:
        return lst
    mid = (left + right)//2
    slow(lst, left, mid)
    slow(lst, mid+1, right)
    if (lst[right] < lst[mid]):
        lst[mid], lst[right] = lst[right], lst[mid]
    slow(lst, left, right-1)
    return lst

def shell(lst):
    n = len(lst)
    gap = n//2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst

import math
import heapq

def intro(lst):
    def partition(lst, low, high):
        pivot = lst[low]
        left = low + 1
        right = high
        done = False
        while not done:
            while left <= right and lst[left] <= pivot:
                left = left + 1
            while lst[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                done = True
            else:
                lst[left], lst[right] = lst[right], lst[left]
        lst[low], lst[right] = lst[right], lst[low]
        return right

    def heapsort(lst, start, end):
        heap = lst[start:end]
        heapq.heapify(heap)
        for i in range(start, end):
            lst[i] = heapq.heappop(heap)

    def introsort(lst, start, end, maxdepth):
        if end - start <= 1:
            return
        if maxdepth == 0:
            heapsort(lst, start, end)
        else:
            pivot = partition(lst, start, end - 1)
            introsort(lst, start, pivot, maxdepth - 1)
            introsort(lst, pivot + 1, end, maxdepth - 1)

    maxdepth = int(math.log2(len(lst))) * 2
    introsort(lst, 0, len(lst), maxdepth)
    return lst
        
algs = {"bubble": bubble, "insertion": insertion, "merge": merge, "selection": selection, "radix": radix, "quick": quick, "tree": tree,"bogo": bogo, "slow": slow, "shell":shell, "intro":intro}

if __name__ == "__main__":
    inp = [4,21,6,45,3,546]
    choice = input("All ('1') or just one('2')? Input:")
    if choice == "1":
        print("Which sorting algorithm would you like?")
        print("")
        option = input("Input: ")
        print(getTime(option, inp))
    else:
        times = {}
        for i in algs:
            res = getTime(i, inp)
            times[i] = res[0]
        print(times)
        print(sorted(times, key=lambda x:x[1]))