class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr , max_val = 0 ,nums[0]
        for i in nums :
            if curr < 0 :
                curr = 0
            curr  += i    
            max_val = max (max_val,curr)    

        return max_val     
