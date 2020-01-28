# Python Program for the Reverse of String without affecting the Position of Special Characters.

# Function For Checking Alphabet.
def is_alpha(x):
    return x.isalpha()

# Swap Function.
def swap(a, b):
    return b, a
# Function for Reverse.
def reverse(string):
    lis = list(string)
    last = len(lis) - 1
    start = 0
    # Traverse List form both end.
    while start < last:
        if not is_alpha(lis[start]):
            start += 1
        elif not is_alpha(lis[last]):
            last -= 1
        else:
            lis[start], lis[last] = swap(lis[start], lis[last])
            start += 1
            last -= 1
    return ''.join(lis)
# Main Function.
def main():
    s = "abec#gh$j%&"
    result = reverse(s)
    print(result)

# Driver code.
if __name__ == "__main__":
    main()