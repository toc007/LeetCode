import string


class Solution(object):
	def longestPalindrome(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		longestPalindrome = s[0]
		for i in range(len(s)):
			sPrime = s[i:]
			lastFoundIndex = string.rfind(sPrime, s[i])
			while lastFoundIndex != -1:
				# palindrome is found
				if self.isPalindrome(sPrime[:lastFoundIndex+1]):
					palindrome = sPrime[:lastFoundIndex+1]
					# if found palindrome is longer, update longest
					if len(palindrome) > len(longestPalindrome):
						longestPalindrome = palindrome
					break
				else:
					lastFoundIndex = string.rfind(sPrime, s[i])


	def isPalindrome(self, s):
		if len(s) == 0 or len(s) == 1:
			return True
		if s[0] == s[-1]:
			return isPalindrome(s[1:-1])
		else:
			return False


Solution().longestPalindrome("helloworld")
