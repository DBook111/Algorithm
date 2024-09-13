def insertion_sort(nums: list[int]):
    """"""
    l = len(nums)
    for i in range(1, l):
        tmp = nums[i]    
        for j in range(i - 1, -1, -1):
            if nums[j] > tmp:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]
            nums[j] = tmp 
            
"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    insertion_sort(nums)
    print("插入排序完成后 nums =", nums)