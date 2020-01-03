# Max Sub Array usando Kadane's Algorithm
#
# https://leetcode.com/problems/maximum-subarray/
# 
# Given an integer array nums, find the contiguous subarray (containing at least one number) which 
# has the largest sum and return its sum
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Código original:  CS Dojo  https://www.youtube.com/watch?v=86CQq3pKSUw
#

def maxSubArray(nums):
    
    # Kadane´s algorithm
    
    length = len(nums)
    if length == 0: return -1
    
    maxsub = nums[0]
    maxglobal = nums[0]
    
    for i in range(1,length):
        
        maxsub = max (nums[i],maxsub + nums[i]) # ou é o atual ou a soma do atual + o max array passado

        if maxglobal < maxsub:
            maxglobal = maxsub
            
    return maxglobal

if __name__ == "__main__":

    a = [-2,1,-3,4,-1,2,1,-5,4]
    print ("Max Sub Array:",maxSubArray(a))