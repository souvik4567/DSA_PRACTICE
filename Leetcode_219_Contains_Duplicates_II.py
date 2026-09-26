class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        seen= {}
        for i,j in enumerate (nums) :
            if j in seen and abs (seen[j]-i) <= k :
                return True
            else :     
                seen[j] = i 
        return False
