""" -----------> Question <---------------
Find Last Digit of a^b for Large Numbers
You are given two numbers. You have to find
the last digit of a^b.
NOTE:
1**2 = 1, 2**2 = 4, 2**3 = 8, 2**4 = 6, 2**5=2,
3**2 = 9, 3**3 = 7, 3**4 = 1, 3**5 = 3, etc.
*-*-*-*-*-*-*-*-*- Example *-*-*-*-*-*-*-
Input: a = 3, b = 10     Output: 9
Input: a = 150, b = 53     Output: 0
Algo:
1) Since nos. are very large store them in str.
2) Take last digit in base a.
3) Now calculate b % 4, Here b is very large.
  a) if b%4 == 0 that means b is completely 
  divisible by 4, so our exponent now will be 
  exp = 4 because by multiplying no 4 times,
  we get the last digit according to cycle table.
  b) If b%4 != 0 means b is not completely 
  divisible by , so our exponent now will be 
  exp = b%4 because by multiplying nos exponent
  times, we get the last digit according to 
  cycle table.
  c) Now calculate last digit = 
        pow(last_digit_in_base, exp).
  d) Last Digit of a^b will be ldigit % 10.
----------------> END <-------------------"""
import math

# Function to find b % a
def modulo(a, b):
    mod = 0
    for i in range(0, len(b)):
        mod=(mod*10 + int(b[i]))%a
    return mod

# Last Digit Function.
def last_digit(a, b):
    len_a = len(a)
    len_b = len(b)
    if (len_a == 1 and len_b == 1 and b[0] == '0' and a[0] == '0'):
        return 1
    if len_b == 1 and b[0] == '0':
        return 1
    if len_a == 1 and a[0] == '0':
        return 0

    if modulo(4, b) == 0:
        exp = 4
    else:
        exp = modulo(4, b)
    res = math.pow(int(a[len_a-1]), exp)
    return int(res % 10)

# Main Function
def main():
    a = "150"
    b = "53"
    print(last_digit(a, b))

if __name__ == "__main__":
    main()