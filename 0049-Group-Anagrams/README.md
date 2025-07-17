Group Anagrams
=========
# Median
Run Time: 13 ms              
Beats: 55.61%      
Time Taken: 12m 27s    
Time Compexity: O(n * k log k)  
(n = number of strings, k = max length of a string → each sort takes O(k log k))    

## Code
```python
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            groups[key].append(s)
            
        return list(groups.values())
```

## 🎯 What is defaultdict(list)?
👉 defaultdict is a special kind of dictionary in Python (from the collections module) that automatically creates a default value for a missing key when you access it.   
     
👉 defaultdict(list) means:   
If you access a key that doesn’t exist yet, Python will automatically create an empty list ([]) for that key.   

## What is ''.join(sorted(s))?
``` python
strs = ["eat","tea","tan","ate","nat","bat"]
result = []
for s in strs:
  result.append(''.join(sorted(s)))
result
```
['aet', 'aet', 'ant', 'aet', 'ant', 'abt']   

Or U can use this code too!
```python
key = str(sorted(s))
```

## Groups are this:
defaultdict(list,
            {'aet': ['eat', 'tea', 'ate'],
             'ant': ['tan', 'nat'],
             'abt': ['bat']})    
      








