import collections
import math
import random

def standard_dev(nums):
    average = sum(nums) // len(nums)
    weighted_average = 0
    for num in nums:
        weighted_average += ((num - average) ** 2)
    weighted_average //= len(nums)
    return int(math.sqrt(weighted_average))

if __name__ == '__main__':
    nums = collections.deque()
    for i in range(30):
        if i < 5:
            nums.append(random.randint(80,100))
        else:
            nums.append(random.randint(140,160))
    print(standard_dev(nums))
