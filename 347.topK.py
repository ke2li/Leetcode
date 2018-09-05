class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        nElements = dict()
        for num in nums:
            temp = nElements.get(num)
            if(temp == None):
                nElements[num] = 1
            else:
                nElements[num] = temp+1
        
        buckets = [list() for i in range(len(nums) + 1)]
        for key, value in nElements.items():
            buckets[value].append(key)
        
        topK = list()
        for i in range(len(nums) + 1, 0, -1):
            if buckets[i-1] :
                for j in buckets[i-1]:
                    topK.append(j)
            if len(topK) == k:
                return topK
            
        return topK

        