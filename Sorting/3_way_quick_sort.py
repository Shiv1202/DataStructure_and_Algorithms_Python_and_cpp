# Implementing 3 way Quick sort on an unsorted array.

def partition3(a, first, end):
  
  x, j, t = a[first], first, end
  i = j
  while i <= t:
    if a[i] < x:
      a[j], a[i] = a[i], a[j]
      j += 1
    elif a[i] > x:
      a[t], a[i] = a[i], a[t]
      t -= 1
      i -= 1
    i += 1
    
  return j, t

def quick_sort(arr, start, end):
  if start >= end:
    return
   
  q1, q2 = partition3(arr, start, end)
  quick_sort(arr, start, q1 - 1)
  quick_sort(arr, q2 + 1, end)
  
  return arr
# Driver Code
A = [4, 9, 4, 4, 1, 9, 4, 4, 9, 4, 4, 1, 4]
print(quick_sort(A, 0, len(A) - 1 ))