class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        order_map = {}
        for i, v in enumerate(order):
            order_map[v] = i

        for i in range(len(words) - 1):
        	word1, word2 = words[i], words[i + 1]

        	# now going through char by char
        	for j in range(len(word1)):
        		# if we reached to the end of word2 before the end of word1
        		if j == len(word2):
        			return False

        		## Let's look for first different char by char
        		if word1[j] != word2[j]:
        			# now we know char is different
        			## now we will check if any one word is less from our key/value from hashmap
        			if order_map[word2[j]] < order_map[word1[j]]:
        				return False

        			break
        return True

# Time complexity is Total number of all characters in words in the input
if __name__ == '__main__':
    s = Solution()
    print s.isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")
    print s.isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")
    print s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")