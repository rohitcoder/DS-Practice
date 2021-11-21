class Solution:
    ## easiest way => Bruteforce way => O(n*n) => O(n)2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n) and Memory O(n) => https://www.youtube.com/watch?v=KLlXCFG5TnA&ab_channel=NeetCode
        # One pass way
        ## we will create hashmap with key as value to index
        ## We will visit each value one by one and if it not matches we will store value and index in hashmap
        prevMap = {} ## val : index

        for index, num in enumerate(nums):
            diff = target - nums
            if diff in prevMap:
                return [prevMap[diff], index]
            prevMap[num] = index
