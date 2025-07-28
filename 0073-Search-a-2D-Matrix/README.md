Search a 2D matrix
=========
# Medium
Run Time: 0 ms           
Beats: 100%      
Time Taken: 47 m  
Time Compexity: O(mn), O(mlog(n)), O(log(mn))   

## Optimal Solution: Time Complexity O(log(mn))
It behaves like a flattened 1D sorted array, so the most optimal solution is to treat it as one sorted list and perform binary search on the entire matrix.   
