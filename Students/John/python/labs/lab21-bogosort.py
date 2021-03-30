"""

all codes are written and created by John Robson Fri Mar 12, 2021

"""

import random

def random_list(n):
    nums = []
    for _ in range(n+1):
        nums.append(random.randint(1, 100))
    return nums
    
def shuffle(nums):
    for n in nums:
        rand = random.randint(0, len(nums) - 1)
        temp = nums[rand]
        nums[rand] = n
        nums[nums.index(n)] = temp
        
    return nums

def is_sorted(nums):
    for n in nums:
        if nums.index(n) < len(nums) - 1 and n > nums[nums.index(n) + 1]:
                return False
    return True

def bogosort(nums):
    while True:
        nums = shuffle(nums)
        check = is_sorted(nums)
        
        if check:
            print(nums)
            break
               
#Advised to not do higher than 5 for quick response time
nums = random_list(5)
bogosort(nums)