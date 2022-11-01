# Task 1
# def twoSum(nums, target: int):
#     dict = {}
#     for i, num in enumerate(nums):
#         match = target - num
#
#         if match in dict:
#             print(dict)
#             return (dict[match], i)
#         else:
#             dict[num] = i
#
#
# nums = [2, 11, 7, 15]
# target = 9
# print(twoSum(nums, target))

#  2nd option
# for i in range(0, len(num_list)):
#     for j in range(i + 1, len(num_list)):
#         if num_list[i] + num_list[j] == 9:
#             print([i, j])
#             break

#  (Optimize Way) Palindrome or not
# def IsPalindrome(x: int):
#     temp = x
#     if x == 0:
#         return True
#     temp_number = 0
#     while temp > 0:
#         num = temp % 10
#         temp_number *= 10
#         temp_number += num
#         temp = temp // 10
#
#     if temp_number == x:
#         return True
#     else:
#         return False
#
#  Less Optimize way
# def isPalindrome(self, x: int) -> bool:
#     bool_value = False
#     temp = x
#     list_x = []
#     if x == 0:
#         return True
#
#     while temp > 0:
#         num = temp % 10
#         temp = temp // 10
#         list_x.append(num)
#
#     size = len(list_x)
#     left = 0
#     right = size - 1
#
#     while left <= right:
#         if list_x[left] == list_x[right]:
#             bool_value = True
#             left += 1
#             right -= 1
#         else:
#             bool_value = False
#             break
#
#     return bool_value

# x = 10201
# print(IsPalindrome(x))

# Roman to integer (Task 13)
def romanToInt(s: str) -> int:
    word = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
    num = 0
    i = 0
    while i < len(s):
        if s[i] in word:
            if i < len(s)-1:
                if (s[i] == 'I' and s[i+1] == 'V') or (s[i] == 'I' and s[i+1] == 'X') or (s[i] == 'X' and s[i+1] == 'L')\
                or (s[i] == 'X' and s[i+1] == 'C') or (s[i] == 'C' and s[i+1] == 'D') or (s[i] == 'C' and s[i+1] == 'M'):
                    num = num + (word[s[i+1]] - word[s[i]])
                    i += 2
                    continue
        num = num + word[s[i]]
        i += 1

    return num

Roman = "MCMXCIV"
print(romanToInt(Roman))
