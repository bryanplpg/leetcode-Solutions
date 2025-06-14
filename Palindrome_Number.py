class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        y=str(x)
        i=0
        j=len(y)-1
        b=True
        while i<(len(y)/2) and j>=len(y)/2 and b:
            if y[i]==y[j]:
                i+=1
                j-=1
            else :
                b=False
        return b

                
