Spiral Matrix
=========
# Median
Run Time: 0 ms              
Beats: 100%      
Time Taken: 25m 54s    
Time Compexity: O(m * n)   

## Visual diagram

Final Spiral Order: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10   

First Layer(While):    
```css
[ 1 →  2 →  3 →  4 ]
[ ↓               ↓ ]
[ 5    6    7    8 ]
[ ↑               ↓ ]
[ 9   10   11   12 ]
[ ↑               ↓ ]
[13 ← 14 ← 15 ← 16 ]
```

Second Layer:
``` css

     [6 → 7]
     [    ↓]
     [10 ←11]

```
I reviewed this code twice!
