# Python Program for find politness of no.
""" *************************************
Politness of a number is defined as the 
number of ways it can be expressed as the
sum of consecutive integers.
NOTE: Input n = 15
      Output = 3
      15 = 1 + 2 + 3 + 4 + 5
      15 = 4 + 5 + 6
      15 = 7 + 8
Naive Approach : By using nested loop, and 
sum every consecutive integer upto n.
Time Complexity : O(n^2)
*****************************************"""
# Efficient Approach is to use factorization.
# We count Odd factors.
# Time Complexity = O(sqrt(n))
# Space Complexity = O(1)

# Function for count Odd Factors.
def count_odd_prime_factor(n):
    result = 1

    # Eliminate all even prime factors.
    while n % 2 == 0:
        n = n / 2
    # at this point n must be odd.
    i = 3
    while i * i <= n:
        div_count = 0
        while n % i == 0:
            n /= i
            div_count += 1
        
        result = result * div_count + 1
        i = i + 2
    # if n odd prime still remains then count it
    if n > 2:
        result = result * 2
    return result

# Function for politness.
def politness(n):
    return count_odd_prime_factor(n) - 1

# Main Function.
def main():
    n = 90
    print("Plitness of " + str(n) + " = " + str(politness(n)))

if __name__ == "__main__":
    main()
