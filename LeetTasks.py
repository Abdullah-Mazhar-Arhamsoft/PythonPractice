# Task 1

def twoSum(nums, target: int):
    dict = {}
    for i, num in enumerate(nums):
        match = target - num

        if match in dict:
            return (dict[match], i)
        else:
            dict[num] = i


nums = [2, 11, 7, 15]
target = 9
print(twoSum(nums, target))

# for i in range(0, len(num_list)):
#     for j in range(i + 1, len(num_list)):
#         if num_list[i] + num_list[j] == 9:
#             print([i, j])
#             break
