# Coin Change 2

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

**Example 1**

```
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
```

**Example 2**
```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
```

**Example 3**
```
Input: amount = 10, coins = [10] 
Output: 1
```

**Note:**

You can assume that
* 0 <= amount <= 5000
* 1 <= coin <= 5000
* the number of coins is less than 500
* the answer is guaranteed to fit into signed 32-bit integer

## Solution

By using Dynamic Programming we make an array to store the no. of ways are possible to form an amount.
* The size of array is of `amount + 1`.
--> Initialize a array of size `amount + 1` with value `0`.
--> update the value of `0th` index as `1`.
--> Now loop through the given coins array and the by using nested loop iterate in range `coin - amount + 1` and update the value of index by adding the value of (index - coin).

Let's go through an example.

**Solution Example**

```
Input: amount = 5, coins = [1, 2, 5]
arr = [0] * (amount + 1)  // [0, 0, 0, 0, 0, 0]
arr[0] = 1               //  [1, 0, 0, 0, 0, 0]
for coin = 1            //   [1, 1, 1, 1, 1, 1]
for coin = 2           //    [1, 1, 2, 2, 3, 3]
for coin = 5          //     [1, 1, 2, 1, 3, 4]
return arr[amount]   //      4
```
