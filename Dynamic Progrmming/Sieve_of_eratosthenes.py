""" -----------> Question <----------------
The classical Sieve of Eratosthenes algorithms
takes O(N log(log N)) time to find all prime
numbers less then N. Your task to reduce it 
to O(N). 
NOTE: Modification,
for every number i where i varies form 2
to N - 1:
Check if the number is prime. If the number
is prime, store it in the prime array.
For every prime numbers j less then or equal
to the smallest prime factor p of i:
Mark all numbers j*p as non_prime.
Mark smallest prime factor of j*p as j.

----------------> END <-------------------"""

max_size = 1000001

is_prime = [True] * max_size
prime = []
SPF = [None] * max_size

# Function to generate all prime number
def seive(n):
    is_prime[0] = is_prime[1] = False
    # Fill rest of the entries.
    for i in range(2, n):
        if is_prime[i]:
            prime.append(i)
            SPF[i] = i      # SPF = Smallest Prime Factor.
        j = 0
        while j < len(prime) and i * prime[j] < n and prime[j] <= SPF[i]:
            is_prime[i * prime[j]] = False
            SPF[i * prime[j]] = prime[j]
            j += 1

# Main Function.
def main():
    n = 13
    seive(n)
    i = 0
    while i < len(prime) and prime[i] <= n:
        print(prime[i], end = " ")
        i += 1

if __name__ == "__main__":
    main()