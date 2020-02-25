""" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
Question : You have an array nums. We
determine two functions to perform on nums.
In both cases, n is the length of nums:

fi(nums) = nums[0] · nums[1] · ... · nums[i-1]·
nums[i+1]·...·nums[n-1].(In other words, 
fi(nums) is the product of all array 
elements except the ithf.)
g(nums) = f0(nums) + f1(nums) + ... +
fn-1(nums).
Using these two functions, calculate all
values of f modulo the given m. Take
these new values and add them together
to get g. You should return the value
of g modulo the given m.
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-"""
# Product Except Self
def productExceptSelf(nums, m):
    l = len(nums)
    f = [1] * l
    temp = 1
    for i in range(1, l):
        f[i] = temp * nums[i - 1]
        temp *= nums[i - 1]
    temp = 1
    for i in range(l-2, -1, -1):
        f[i] *= temp*nums[i+1]
        temp *= nums[i + 1]
    for i in range(len(f)):
        f[i] = f[i] % m
    return sum(f)%m


# Main Function.
def main():
    s = 12
    arr = [1, 2, 3, 7, 5]
    res = productExceptSelf(arr, s)
    print(res)

# Driver Code.
if __name__ == "__main__":
    main()
