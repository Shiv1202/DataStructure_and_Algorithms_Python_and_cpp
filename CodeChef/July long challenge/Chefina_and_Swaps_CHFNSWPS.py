import collections

def solution(a, b, n):
    if sorted(a) == sorted(b):
        return 0
    
    freq_a = dict(collections.Counter(a))
    freq_b = dict(collections.Counter(b))
    for i in freq_a:
        if i not in freq_b:
            if freq_a[i] % 2 != 0:
                return -1
        else:
            if (freq_a[i] + freq_b[i]) % 2 != 0:
                return -1
    for i in freq_b:
        if i not in freq_a:
            if freq_b[i] % 2 != 0:
                return -1

    m = min(min(a), min(b))
    
    a.sort(); b.sort();
    i, j= 0, 0
    final_swap_can = []
    swap_can = []
    
    while i < n and j < n:
        if a[i] == b[j]:
            i += 1; j += 1
        elif a[i] < b[j]:
            swap_can.append(a[i])
            i += 1
        elif b[j] < a[i]:
            swap_can.append(b[j])
            j += 1
        if i > n - 1:
            swap_can.extend(b[j:n])
            i += 1
        elif j > n - 1:
            swap_can.extend(a[i:n])

    for i in range(0, len(swap_can), 2):
        final_swap_can.append(swap_can[i])
    final_swap_can.sort()

    cost = 0
    for i in range(len(final_swap_can) // 2):
        if final_swap_can[i] == m:
            cost += m
        elif final_swap_can[i] <= 2 * m:
            cost += final_swap_can[i]
        else:
            cost += 2 * m 
    return cost

def main():
    for _ in range(int(input())):
        n = int(input())
        arr_a = list(map(int, input().split()))
        arr_b = list(map(int, input().split()))
        print(solution(arr_a, arr_b, n))

if __name__ == "__main__":
    main()



    