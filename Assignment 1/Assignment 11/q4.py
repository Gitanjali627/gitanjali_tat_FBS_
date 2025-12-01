nums = [12, 45, 2, 10, 67, 33]

# Bubble Sort
for i in range(len(nums)):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print("Second Largest:", nums[-2])