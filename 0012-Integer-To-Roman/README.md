
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
1. Subtract **the largest possible value** from the number.
2. For each process, append the corresponding Romans to the result.   
EX) num = 3749
1) i = 0    
num = 3749 - 1000 -1000 - 1000 = 749  
result = MMM     
2) i = 1    
num = 749 - 500  = 249    
result = MMMD


