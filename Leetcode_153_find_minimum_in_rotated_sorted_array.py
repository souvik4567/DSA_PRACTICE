class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        mid = (left + right)/2
        
        while left < right:
            
            if nums[mid] > nums [right]:
                left = mid+1
            else : 
                right = mid
            mid = (left + right)/2
            
        return nums[mid]               
