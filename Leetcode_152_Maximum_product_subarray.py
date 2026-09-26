class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max,curr_min = nums[0],nums[0]
        max_val = nums[0]
        for i,num in enumerate (nums):
            if i== 0:
                curr_max, curr_min= num,num
            else:
                temp = max(curr_max*num,num,curr_min*num)
                curr_min = min(curr_min*num,num,curr_max*num)
                curr_max=temp

            max_val = max(max_val,curr_max)

        return max_val    
