3 Sum Closet
=========
# Median
## Soultion
Run Time: 379ms        
Beats: 24.83%        
Time Taken: 42m 28s        
Time Compexity: O(N^2)   

## My mistake
I made mistake that return best solution!    
### **Wrong Code**  
```python
if total == target:
    left += 1
    right =- 1
```
### *Right Code*
``` python
if total == target:
    return total
```

### What is this code?
This code uses a lot when you find the minimum or maximun value!  
``` python
closet = float('inf') # positive infinite\
```

### Don't forget to sort nums!  

