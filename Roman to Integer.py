class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicti={"I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
        total=0
        prev_numb=0
        for i in reversed(s):
            numb=dicti[i]
            if numb<prev_numb:
                total-=numb
            else :
                total+=numb
                prev_numb=numb
        return total
                
     






