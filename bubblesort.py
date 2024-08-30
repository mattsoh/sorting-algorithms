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
      
import time
from datetime import timedelta
start_time = time.monotonic()
start = time.process_time()

print(bubble([4,21,6,45,3,546]))
end_time = time.monotonic()
# print(timedelta(seconds=end_time - start_time))    
elapsed = (time.process_time() - start)
print(elapsed)
print(insertion([4,21,6,45,3,546])) 