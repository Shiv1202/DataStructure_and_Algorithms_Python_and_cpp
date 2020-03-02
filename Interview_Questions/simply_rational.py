""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Question : There are many different tuples
representing the same rational number.
For instance, one-half is (1, 2), (2, 4),
(3, 6), etc. Your task is to write a
function that, given the numbers numerator
and denominator representing the ratio
numerator / denominator, returns an array
[a, b] of two integers where:
(a, b) represents the same rational number
as (numerator, denominator) but in simplified 
format;
a and b have no non-trivial factors;
b is positive
************** Example ****************
The number 3 / 6 can be reduced to 1 / 2.
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""

# Rational Function.
def simplifyRational(numerator, denominator):
    g=math.gcd(numerator, denominator)
    m, n = numerator/g, denominator/g
    if n < 0:
        return [-m, -n]
    return [m, n]

# Main Function.
def main():
    n = 3
    d = 6
    res = simplifyRational(n, m)
    print(res)

#Driver Code.
if __name__ == "__main__":
    main()