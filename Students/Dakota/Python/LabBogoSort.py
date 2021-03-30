#Lab Bogo Sort
import random

def random_list(n):
    temp_list = []
    for _ in range(n):
        temp_list.append(random.randint(1, 100))
    return temp_list

def shuffle(nums):
    for x in nums:
        r = random.randint(0,len(nums)-1)
        t = nums[r]
        nums[r] = x
        nums[nums.index(x)] = t
    return nums

def is_sorted(nums):
    for x in range(len(nums)-1):
        if nums[x] > nums[x+1]:
            return False
    return True        

def bogosort(nums):
    while not is_sorted(nums):
        nums = shuffle(nums)
    print(nums)
           
r_list = random_list(5)
bogosort(r_list)