
Longest commom prefix
=========
# Easy
## Soultion
Run Time: 0ms    
Beats: 100%    
Time Taken: 10m 34s    
Time Compexity: O(N * M)  

### What is startswith()?
```python
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x) ## True
```
It checks whether txt starts with 'Hello' or not.  

### Explanation
'''python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix
'''

1. Assume that prefix is in strs[0]   
2. if other words does not start with predfix, minus a last letter
EX) prefix = flower -> flowe -> flow ...   

