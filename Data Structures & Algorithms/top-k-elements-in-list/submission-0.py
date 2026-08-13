from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m=defaultdict(int)
        for n in nums:
            m[n]+=1
        m=sorted(m.items(), key=lambda n:n[1], reverse=True)
        return [n[0] for n in m[:k]]