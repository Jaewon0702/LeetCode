Count and Say
=========
# Median
Run Time: 7ms        
Beats: 73.01%      
Time Taken: 49m 36s      
Time Compexity: O(2^lnN) = ExponentialInN  

## How to use recursive function
```python
def countAndSay(self, n: int) -> str:
    prev = self.countAndSay(n - 1) # How to use recursive function
    result = ""
```
## What is itertools.groupby() function?
It returns digit and it's coutings(how many digits are together?)

```python
import itertools
prev = 11112222333
for digit,group in itertools.groupby(str(prev)):
  print(digit, list(group))
```    
Output:    

```
1 ['1', '1', '1', '1']    
2 ['2', '2', '2', '2']   
3 ['3', '3', '3']   
```
I reviewed this code!   
