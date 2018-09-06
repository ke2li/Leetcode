class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        currLength = 0
        occurred = dict()
        j = 0

        for i, char in enumerate(s):
            if char not in occurred:
                occurred[char] = i
                longest = max(i - j + 1, longest)
            else:
                if(j <= occurred[char] + 1):
                    j = max(occurred[char] + 1 , j)
                else:
                    longest = max(i - j + 1, longest)
                occurred[char] = i
                
        return longest
