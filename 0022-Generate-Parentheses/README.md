
Generate Parentheses
=========
# Median
## Soultion
Run Time: 0ms      
Beats: 100%      
Time Taken: 4m 30s      
Time Compexity: O(4^N/Sqrt(N))  
### Explanation
1. Add an '(' if you haven’t used all n opens.  
2. Add a ')' if it won't exceed the number of '(' used.  
3. When your string reaches length 2 * n, you have a valid combo.
4. So add a valid come combo to a result list
### Visiulization
```arduino
       ""
      /   \
     (     (       ← 2 open choices
    / \   / \
  (( () () (
   |   |   \
(() (())  ()(
           \
           ()()

```
Review 2
