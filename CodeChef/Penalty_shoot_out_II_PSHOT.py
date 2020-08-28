for _ in range(int(input())):
    n = int(input())
    turn = input()
    hit_a, hit_b = 0, 0
    turn_a = turn_b = n
    flag = True
    for i in range(2 * n):
        if turn[i] == '1':
            if 1 & i:
                hit_b += 1
            else:
                hit_a += 1
        if i & 1:
            turn_b -= 1
        else:
            turn_a -= 1

        if hit_a + turn_a < hit_b:
            print(i + 1)
            flag = False
            break
        if hit_b + turn_b < hit_a:
            print(i + 1)
            flag = False
            break
    if flag:
        print(n * 2)