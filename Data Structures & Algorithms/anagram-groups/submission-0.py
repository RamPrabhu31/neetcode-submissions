class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        result =[]
        for i in strs:
            k="".join(sorted(i))
            if k not in dict1:
                dict1[k] = []
            dict1[k].append(i)

        for values in dict1.values():
            result.append(values)
        return result