class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n=len(nums)
        closestSum=float('inf')

        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                continue
            low,high=i+1,n-1
            while low<high:
                currentSum=nums[i]+nums[low]+nums[high]
                if abs(currentSum-target)<abs(closestSum-target):
                    closestSum=currentSum
                if currentSum==target:
                    return currentSum
                elif currentSum<target:
                    low+=1
                else:
                    high-=1
        return closestSum




# Example of the class 

solution=Solution()

print(solution.threeSumClosest([2,4,5,9,7,8],12))