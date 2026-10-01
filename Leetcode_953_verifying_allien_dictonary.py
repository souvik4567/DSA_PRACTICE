class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        catalogue = {}    
        for i in range (len(order)):
            catalogue[order[i]]=i
        j=0
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            min_length = min (len(w1),len(w2))

            for j in range (min_length):
                if w1[j] <> w2[j]:
                    if catalogue[w1[j]] > catalogue[w2[j]]:
                        return False
                    else :
                        break
            else :   #This else block works as an for loop completion check, i.e if the loop ends we check the size of the words as first word always has to be smaller
                if len(w1) > len(w2):
                    return False            
        return True




            
