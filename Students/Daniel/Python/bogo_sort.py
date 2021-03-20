import random
random_nums = []
range_list = list(range(0,101))

def random_list(n):
    for x in range(n):
        random_nums.append(random.choice(range_list))


def shuffle(nums):
    temp_list = []
    index_list = list(range(0,len(nums)))
    random.shuffle(index_list)
    for item in range(len(nums)):
        temp_list.append(nums[index_list[item]])
    return temp_list








def is_sorted(nums):

    for item in range(1,len(nums)-1):
        if nums[item-1] < nums[item] < nums [item + 1]:
            pass
        else:
            return False

    print(f"We did it!: {nums}")
    return True
    

def bogosort(list_len, nums):
    random_list(list_len)
    while is_sorted(nums) != True:
        nums = shuffle(nums)


bogosort(4,random_nums)