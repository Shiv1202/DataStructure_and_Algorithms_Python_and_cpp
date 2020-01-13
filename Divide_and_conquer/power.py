# Python Program for finding pow(x, y) By using Divide and Conqure.
""" ************************************
NOTE: This is based on Divide and Conqure 
Algorithm.
Below solution divides the problem into
subproblems of size y/2 and call the 
subproblems recursively.
NOTE: This code is also work for the 
    float value of x and negative value 
    of y.
Time Complexity : O(log(n))
Space Complexity : O(1)
****************************************"""
# The Power Function.
def power(x, y):
    if y == 0:
        return 1
    temp = power(x, int(y / 2))
    # If y is Even.
    if y % 2 == 0:
        return temp * temp
    else:
        # If y is a positive no.
        if y > 0:
            return x * temp * temp
        else:   # If y is a negative no.
            return (temp * temp) / x

# Main Function.
def main():
    x, y = 2, 3
    print('%.6f' %(power(x, y)))

# Driver Code.
if __name__ == "__main__":
    main()