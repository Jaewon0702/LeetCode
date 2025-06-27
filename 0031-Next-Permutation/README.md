Next Permutation
=========
# Medium
## Soultion
Run Time: 0ms        
Beats: 100%      
Time Taken: 50m 49s      
Time Compexity: O(N)

## How it works?
🔹 Step 1: Find the first decreasing element from the end   
``` yaml
Index:     0   1   2
Values:   [1,  3,  2]
                ↑    ← nums[2] = 2
            ↑         ← nums[1] = 3 (3 > 2 ❌)

Now check:
nums[0] = 1 < nums[1] = 3 ✅
→ So, i = 0

```
🔹 Step 2: Find the next larger element after index i   
nums[2] = 2 > nums[0] = 1 ✅  
→ So, j = 2  

🔹 Step 3: Swap nums[i] and nums[j]
``` python
Before swap: [1, 3, 2]
After swap:  [2, 3, 1]

```
🔹 Step 4: Reverse the subarray after index i  
``` python
Subarray before: [3, 1]
Reverse it:      [1, 3]

Final list: [2, 1, 3]

```
Both solution 1 and solution 2 have difference under if i >= 0: code!  
Funny thing is that both codes work!


