#brute force method, times out on case 19
# class Solution:
#     def ladderLength(self, beginWord, endWord, wordList):
#         """
#         :type beginWord: str
#         :type endWord: str
#         :type wordList: List[str]
#         :rtype: int
#         """
#         steps = (-1)
#         for word in wordList:
#             if self.diff1(beginWord, word):
#                 traversedList = list()
#                 self.helper(word, endWord, wordList, traversedList, steps)

#         if steps != -1:
#             return steps
#         return 0

#     def helper(self, currWord, endWord, wordList, traversedList, steps):
#         if len(traversedList) + 2 >= steps[0] and steps[0] != -1:
#             return

#         if currWord == endWord:
#             steps[0] = len(traversedList) + 2
#             return

#         for word in wordList:
#             if word not in traversedList:
#                 if self.diff1(currWord, word):
#                     newList = traversedList.copy()
#                     newList.append(currWord)
#                     self.helper(word, endWord, wordList, newList, steps)
                    
#     def diff1(self, a, b):
#         numDiff = 0
#         for i, char in enumerate(a):
#             if char != b[i]:
#                 numDiff += 1

#         return numDiff == 1   

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        traversedList = set()
        currWords = list(beginWord)
        newWordList = list()
        nextWords = list()
        dis = 2
        while(True):
            if len(wordList) == 0:
                return 0
            for currWord in currWords:
                for word in wordList:
                    if self.diff1(currWord, word):
                        if word == endWord:
                            return dis
                        nextWords.append(word)
                    else:
                        newWordList.append(word)

            wordList = newWordList
            currWords = nextWords
            newWordList = list()
            nextWords = list()
            dis +=1

        return 0
                    
    def diff1(self, a, b):
        numDiff = 0
        for i, char in enumerate(a):
            if char != b[i]:
                numDiff += 1

        return numDiff == 1



class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        traversed = set()
        tryWords = list()
        tryWords.append(beginWord)
        nextTry = list()
        distance = 2
        while(True):
            if len(tryWords)==0:
                return 0

            for curr in tryWords:
                for word in wordList:
                    if word not in traversed:
                        if self.diff1(curr,word):
                            if word == endWord:
                                return distance
                            nextTry.append(word)
                        else:
                            nextWordList.append(word)
                            traversed.add(word)

            tryWords = nextTry
            nextTry = list()
            distance += 1

    def diff1(self, a, b):
        numDiff = 0
        for i, char in enumerate(a):
            if char != b[i]:
                numDiff += 1

        return numDiff == 1