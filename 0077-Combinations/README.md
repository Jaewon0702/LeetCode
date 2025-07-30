Combinations
=========
# Medium
Run Time: 137 ms         
Beats: 53.70%       
Time Taken: 27m 42s  
Time Compexity: O(K∗C(N,K))
Space Complexity : O(C(N,K))  

## What's different comparing to permutations algorithm?

I have to avoid duplicates
```less
Start with backtrack(1, [])

        []
     /   |   |   \
   [1] [2] [3] [4]
    |
  backtrack(2, [1])
     |
    [1,2] ✅
    [1,3] ✅
    [1,4] ✅

From [1] we explore:

  [1] → [1,2] ✅ (length = 2 → save)
      → backtrack(3, [1,2])
        - Skipped (already length 2)

  [1] → [1,3] ✅
  [1] → [1,4] ✅


From [2]:

  [2] → [2,3] ✅
  [2] → [2,4] ✅

From [3]:

  [3] → [3,4] ✅

From [4]:
  Nothing (can’t pick 2 numbers from here)


✔️ Final combinations:
- [1,2]
- [1,3]
- [1,4]
- [2,3]
- [2,4]
- [3,4]

```
