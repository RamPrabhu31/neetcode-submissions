class Solution:

    def encode(self, strs: List[str]) -> str:
        string =""
        for i in strs:
            string = string+str(len(i))+'#'+i
        return string

    def decode(self, s: str) -> List[str]:
        result=[]
        i=0
        
        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            lenght = int(s[i:j])
            i=j+1
            result.append(s[i:i+lenght])
            i=i+lenght
        return result