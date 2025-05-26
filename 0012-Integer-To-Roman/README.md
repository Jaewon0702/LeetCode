
Integer to Roman
=========
# Median
## Soultion 
Run Time: 4ms     
Beats: 64.62%     
Time Taken: 30m 1s       
Time Compexity: O(1)   
### Explanation
``` python
class Solution:
    def intToRoman(self, num: int) -> str:
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL','X','IX','V','IV','I']
        result = ""
        for i in range(len(val)):
            while num >= val[i]:
                num -= val[i]
                result += sym[i]
        return result
```

