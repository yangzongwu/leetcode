### [319\. Bulb Switcher](https://leetcode.com/problems/bulb-switcher/)

Difficulty: **Medium**


There are _n_ bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the _i_-th round, you toggle every _i_ bulb. For the _n_-th round, you only toggle the last bulb. Find how many bulbs are on after _n_ rounds.

**Example:**

```
Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.
```


#### Solution

Language: **Python3**

```python3
class Solution:
    def bulbSwitch(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        l,r=1,n
        while l<=r:
            mid=(l+r)//2
            if mid**2==n:
                return mid
            elif mid**2>n:
                r=mid-1
            else:
                l=mid+1
        return r
```
