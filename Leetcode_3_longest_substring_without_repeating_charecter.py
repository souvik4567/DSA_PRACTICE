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

                seen = {}
        '''
        #hash Map approach
        
        left, max_length = 0, 0
        for i,ch in enumerate(s):
            if ch in seen and seen[ch]>=left:                 # this check is requred to make sure we are checking under window or not
                left = seen[ch]+1
            seen[ch] = i    
            max_length = max(i-left+1,max_length)
        return max_length
        '''
