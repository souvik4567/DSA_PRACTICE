class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashtable = set()

        for i in nums :
            if i in hashtable :
                return True
            else :
                hashtable.add(i)
        return False
