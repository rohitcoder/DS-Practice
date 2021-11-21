class solution:
	def addBinary(self, a, b):
		carry = 0
		result = ""

		a, b = list(a), list(b)

		while a or b or carr == 1:
			if a:
				carry + =int(a.pop())
			if b:
				carry += int(b.pop())

			result += carry % 2
			carry = carry // 2
		return result[::-1]

class solution:
	def addBinary(self,a ,b):
		return bin(int(a,2) + int(b,2))[2:]