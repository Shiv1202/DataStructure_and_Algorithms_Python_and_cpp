# Python Program for Reverse of a String Using Recursion
# Function for Print Reverse.
def reverse_string(s):
    if len(s) == 0:
        return
    temp = s[0]
    reverse_string(s[1:])
    print(temp, end = " ")

# Main function.
def main():
    string = "Hello World!!"
    reverse_string(string)

if __name__ == "__main__":
    main()