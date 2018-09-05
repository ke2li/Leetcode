class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        row = [[] for i in range(numRows)]

        UpOrDown = 1
        currRow = 0
        for char in s:
        	row[currRow].append(char)
        	if currRow == 0:
        		UpOrDown = 1
        	elif currRow == numRows - 1:
        		UpOrDown = -1
        	currRow += UpOrDown 

        returnString = ''
        for i in row:
        	returnString += ''.join(i)

        return returnString