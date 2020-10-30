from typing import List
def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums)
    while left < right: 
        mid = (left + right) // 2;
        if(nums[mid] < target):
            left = mid + 1
        elif(nums[mid] > target):
            right = mid
        else:
            return mid
    return -1

def main():
    nums = [1, 2, 3, 4, 5 ]
    index = search(nums, 3)
    print("index ", index)

if __name__ == '__main__':
    main();