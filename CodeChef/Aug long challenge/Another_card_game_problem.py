import math
def solution(c, r):
    digit_c = math.ceil(c / 9.0)
    digit_r = math.ceil(r / 9.0)

    if digit_r <= digit_c:
        return f"1 {digit_r}"
    else:
        return f"0 {digit_c}"

for _ in range(int(input())):
    c, p = map(int, input().split())

    print(solution(c, p))