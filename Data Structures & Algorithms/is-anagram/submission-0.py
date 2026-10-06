class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1={}
        for i in s:
            dict1[i]=dict1.get(i,0)+1

        for j in t:
            dict1[j]=dict1.get(j,0)-1

      
        for key,values in dict1.items():
            if values != 0:
                return False
        return True