class Solution:
	## easiest way => Bruteforce way => O(n*n) => O(n)2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

    # Efficient WAY => O(n)
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		## Let's take a left, right pointer and we will keep shifting it until we find soltuion
		## We will elimitate the bigger numbers from right just to improve calculation because numbers is sorted
		l, r = 0, len(numbers) - 1

		while l < r:
			currSum = numbers[l] + numbers[r]

			if currSum > target:
				r -= 1 # Shifting right pointer to left
			elif currSum < target:
				l += 1 # Shifting left pointer to right
			else:
				return [l+1, r+1]
