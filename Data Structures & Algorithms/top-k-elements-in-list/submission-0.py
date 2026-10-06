class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1={}
        for i in nums:
            dict1[i]=dict1.get(i,0)+1

        high = dict(sorted(dict1.items(), key=lambda  x:x[1], reverse =True))
        
        w=list(high.keys())
        return w[:k]