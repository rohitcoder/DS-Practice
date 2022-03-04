class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # https://www.youtube.com/watch?v=jzZsG8n2R9A&ab_channel=NeetCodee
        # Time complexity => O(n*n) => O(n)2
        # Space complexity => O(1) or O(n) because sorting does take extra memory based on lib you use
        #first we will sort it to prevent duplicates and adjust left, right pointers

        res = []
        nums.sort() # sorting array

        for index, value in enumerate(nums):
            ## value == nums[i-1] is means equal to value so we don't want to check this 
            ## to avoid duplicate let's continue to next part
            if index > 0 and value == nums[index-1]:
                continue

            l, r = index+1, len(nums) - 1 # setting up pointers
            while l<r:
                threeSum = value + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1 # shifting right pointer 1 back
                elif threeSum <0 :
                    l += 1 # shifting left pointer 1 front
                else:
                    res.append([value, nums[l], nums[r]])

                    ## Now we will shift values inside result to avoid duplicates

                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        ## This means same value, so keep shifting pointer.
                        ## We don't want left pointer to ever pass right pointer so add condition
                        l += 1
        return res



