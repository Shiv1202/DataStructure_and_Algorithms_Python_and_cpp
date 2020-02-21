""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
You have two integer arrays, a and b, and an
integer target value v. Determine whether
there is a pair of numbers, where one number
is taken from a and the other from b, that
can be added together to get a sum of v.
Return true if such a pair exists, otherwise
return false.
------------------> Example <---------------
For 
a = [1, 2, 3], b = [10, 20, 30, 40],
and v = 42, the output should be
sumOfTwo(a, b, v) = true.
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""

# sumOfTwo function.
def sumOfTwo(a, b, v):
    complements = set()
    for i in range(len(a)):
        complements.add(v - a[i])
    for i in b:
        if i in complements:
            return True
    return False
        
# Main Function.
def main():
    a = [1, 2, 3]
    b = [10, 20, 30, 40]
    v = 42
    print(sumOfTwo(a, b, v))

# Driver Code.
if __name__ == "__main__":
    main()