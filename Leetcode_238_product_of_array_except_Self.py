class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        pre = 1
        post = 1 

        ans = []

        for i in range (len(nums)):
            ans.append (pre)
            pre *= nums[i]

        for i in range (len(nums)-1,-1,-1):
            ans[i] *= post
            post *= nums[i]
        return ans
       
