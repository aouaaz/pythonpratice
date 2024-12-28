import time

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
    
    
    def moveZeroes2(self, nums: list[int]) -> list[int]:
        
        first_index_non_zero = 0
        for num in range(len(nums)):
            if num != 0:
                num , nums[first_index_non_zero] = nums[first_index_non_zero], num
                first_index_non_zero += 1
                
        return nums 
            
    
    def majorityElements(self, nums: list[int]) -> int:
        my_map = {}
        for item in nums:
            my_map[item] = my_map.get(item, 0) + 1
            if (my_map[item] >= len(nums)/2):
                return item
            print(f"the map is  {my_map}")
        maximum = max(my_map.values())
        return maximum
            
    
            
            
            
            
            
            
def main():
    # Moving Zeros testing 
    num = [0,0,1,2,3,0,0]
    num = [0,0,1,2,0,0,0,3,0]
    test = Solution()
    start_time = time.time()
    result = test.moveZeros(num)
    print(f"the output list is {result}")
    end_time = time.time()
    print(f"Original was  {num}")
    print(f"elapsed time of moveZero1 : {end_time- start_time}")
    start_time = time.time()
    result = test.moveZeroes(num)
    end_time = time.time()
    print(f"the output list is {result}")
    print(f"elapsed time of moveZero1 : {end_time- start_time}")
    start_time = time.time()
    result = test.moveZeroes2(num)
    end_time = time.time()
    print(f"the output list is {result}")
    print(f"elapsed time of moveZero1 : {end_time- start_time}")
    
    # Finding majority of elements
    num = [2,2,2,1,1,1,2,2,2]
    num = [3,2,3]
    

    result = test.majorityElements(num)
    print(f"The majority elements of {num} is {result}")
         


if __name__ == "__main__" :
    main()