# Python Program for find LCM of given array.
""" ***********************************
Input : {1, 2, 8, 3}
Output : 24
Input : {2, 7, 3, 9, 40}
Output : 252
NOTE: We Know
LCM(a, b) = (a * b) / gcd(a, b)
The above relation is not valid for 3 no.
The Main idea of Algorithms are:
1) Initilize ans = arr[0]
2) Iterate over all the element of the 
    array i.e. from i = 0 to i = n -1
    At the ith iteration ans = LCM(arr[0]..
    , arr[1], ........., arr[i - 1]).
    This cen be done easily as 
    LCM(arr[0], arr[1],...... , arr[i]) = 
    LCM(ans, arr[i]). Thus at i'th iteration 
    we just have to do ans = LCM(ans, arr[i])
     = ans * arr[i] / gcd(ans, arr[i])
***************************************"""
# Function for Finding LCM.
def find_lcm(num1 , num2):
    if num1 > num2:
        num = num1
        temp = num2
    else:
        num = num2
        temp = num1
    rem = num % temp
    while rem != 0:
        num = temp
        temp = rem
        rem = num % temp
    gcd = temp
    lcm = int(int(num1 * num2) / int(gcd))
    return lcm

# Main Function
def main():
    arr = [20, 7, 13, 19, 4]
    num1 = arr[0]
    num2 = arr[1]
    lcm = find_lcm(num1, num2)
    for i in range(2, len(arr)):
        lcm = find_lcm(lcm, arr[i])
    print(lcm)

if __name__ == "__main__":
    main()
