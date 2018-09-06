class Solution:
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        differences = list()
        for i in range(len(nums) - 1):
        	differences.append(nums[i+1] - nums[i])

        maxLength = len(nums)

        if len(nums) <= 1:
        	return len(nums)
        
        if differences[0] == 0:
            maxLength -=1
        
        currPos = 1
        while(currPos < len(differences)):
            if differences[currPos] == 0:
            	differences[currPos] = differences[currPos -1]
            	maxLength -=1
            elif differences[currPos] < 0:
            	if differences[currPos - 1] < 0:
                    differences[currPos] += differences[currPos - 1]
                    maxLength -=1
                    
            elif differences[currPos] > 0:
           		if differences[currPos - 1] > 0:
           			differences[currPos] += differences[currPos - 1]
           			maxLength -=1
            currPos += 1

        return maxLength

