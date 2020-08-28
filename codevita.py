import itertools
def solution(start, end, k):
  a = [i for i in range(start, end + 1)]
  ans = 0
  x = itertools.product(a, repeat = k)
  for group in x:
    if sum(group) % 2 == 0:
      ans = ans + 1
  return ans % 100000007
#def s(tup):
  #pass
start, end = map(int, input().strip().split())
k = int(input())
print(soulution(start, end, k))


