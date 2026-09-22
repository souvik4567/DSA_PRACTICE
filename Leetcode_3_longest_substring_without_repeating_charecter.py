class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0 :
            return 0
        if len(s) ==1 :
            return 1 

        seen=set()
        left,right,max_length, = 0,0,0


        while right < len(s):
            if s[right] not in seen :
                seen.add(s[right])
                max_length = max (max_length,right-left+1)
                right += 1
            else :
                seen.remove(s[left])
                left +=1 
        return max_length
