class Solution:
    def moveZeros(self, nums: list[int]) -> list[int]:
        j = len(nums) - 1 
        for i, num in enumerate(nums):
            if num == 0:
                while j > i and nums[j] == 0:
                    j -= 1
                print(f"swapping {nums[i]} with {nums[j]}")
                nums[j], nums[i] = nums[i], nums[j]
            if i >= j:
                return nums
    
    
    def moveZeroes(self, nums: list[int]) -> list[int]:
        for i, num in enumerate(nums):
            j = i
            while j < len(nums) and nums[j] == 0:
                j += 1
            if i < len(nums) and j < len(nums) and num == 0:
                print(f"swapping number between i : {i} and number is {num} other j : {j} number is {nums[j]} ")
                nums[i], nums[j] = nums[j], nums[i]
        return nums
            
            
            
            
            
def main():
    num = [0,0,1,2,3,0,0]
    num = [0,0,1,2,0,0,0,3,0]
    
    test = Solution()
    print(f"Original was  {num}")
    result = test.moveZeroes(num)
    print(f"the output list is {result}")
         


if __name__ == "__main__" :
    main()