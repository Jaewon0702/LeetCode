Roman to Integer
=========
# Easy
## Soultion 
Run Time: 8ms   
Beats: 27.81%   
Time Taken: 47m 1s     
Time Compexity: O(N) 

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100,
            'D' : 500, 'M' : 1000, 'IV' : 4, 'IX' : 9, 'XL' : 40,
            'XC' : 90, 'CD' : 400,'CM' : 900
        }
        result = 0
        i = 0
        while i < len(s):
            # check for pairs!
            if (i+1 < len(s) and dic[s[i]] < dic[s[i+1]]):
                result += dic[s[i] + s[i+1]]
                i+=2
            else:
                result += dic[s[i]]
                i += 1
        return result
```

There is a rule in pairs of numbers: the previous number is smaller than the next number.  

