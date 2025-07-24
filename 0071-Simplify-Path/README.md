Simplify Path
=========
# Medium
Run Time: 4 ms         
Beats: 16.75%      
Time Taken: 47 m
Time Compexity: O(N) 

## Understanding of rules
The simplified canonical path  
1. '.'  
/d/./ -> /d//
2. '..'
/d/../ -> ///

## How did I solve?
Split the path with '/'  
And use a stack!  
 
