3 Sum
=========
# Median
## Soultion
Run Time: 601ms      
Beats: 98.68%      
Time Taken: 30m 34s      
Time Compexity: O(N^2)  

### Why this works
- Sort first: ensures duplicates can be skipped easily.

- For each nums[i], use two pointers (left, right) to find the pair that makes the sum 0.

- Skip duplicates along the way to ensure uniqueness.

Review 1
