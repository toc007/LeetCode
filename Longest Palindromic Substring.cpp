class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		longestPalindrome = ""
		for i in range(len(s)):
			L = i-1
			R = i+1
			while L >= 0 and R < len(s):
				if s[L] != s[R]:
					break
				L -= 1
				R += 1
			if R-L-1 > len(longestPalindrome):
				longestPalindrome = s[L+1:R]
		for i in range(len(s)):
			L = i-1
			R = i+2
			if i+1 < len(s) and s[i] == s[i+1]:
				while L >= 0 and R < len(s):
					if s[L] != s[R]:
						break
					L -= 1
					R += 1
				if R-L-1 > len(longestPalindrome):
					longestPalindrome = s[L+1:R]
		return longestPalindrome

print Solution().longestPalindrome("cbbd")