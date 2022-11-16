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
# def romanToInt(s: str) -> int:
#     word = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, }
#     num = 0
#     i = 0
#     while i < len(s):
#         if s[i] in word:
#             if i < len(s)-1:
#                 if (s[i] == 'I' and s[i+1] == 'V') or (s[i] == 'I' and s[i+1] == 'X') or (s[i] == 'X' and s[i+1] == 'L')\
#                 or (s[i] == 'X' and s[i+1] == 'C') or (s[i] == 'C' and s[i+1] == 'D') or (s[i] == 'C' and s[i+1] == 'M'):
#                     num = num + (word[s[i+1]] - word[s[i]])
#                     i += 2
#                     continue
#         num = num + word[s[i]]
#         i += 1
#
#     return num
#
# Roman = "MCMXCIV"
# print(romanToInt(Roman))


# Longest Common prefix (Task 14)
# def longestCommonPrefix(strs: list[str]) -> str:
#
#     minimum = min(map(len, strs))
#     word = ""
#
#     for a in range(minimum):
#         for b in range(1, len(strs)):
#             if strs[0][a] == strs[b][a]:
#                 ask = True
#                 print("True")
#             else:
#                 ask = False
#                 break
#         if ask:
#             word = word + strs[0][a]
#             print("wo: ", word)
#         else:
#             break
#
#     return word
#
# st = ["c","acc","ccc"]
# longestCommonPrefix(st)

# Remove duplicate from sorted array(Task 26)
# def removeDuplicates(nums: list[int]) -> int:
#     i = 0
#     while i < len(nums) - 1:
#         if nums[i] == nums[i + 1]:
#             nums.remove(nums[i])
#             i -= 1
#         i += 1
#
#
# nums = [0, 0, 1, 1, 1, 2, 2]
# removeDuplicates(nums)

# plus One(Task 66)
# def plusOne(digits: list[int]) -> list[int]:
#     num = 0
#     for i in digits:
#         num = (num + i)*10
#
#     num = (num // 10) + 1
#     print([int(item) for item in str(num)])
#
# nums = [9,9,9]
# plusOne(nums)

# Square root (Task 69)
# def mySqrt(x: int) -> int:
#     val = x
#     count = 0
#     n = 1
#     while val - n >= 0:
#         val -= n
#         n += 2
#         count += 1
#
#     print(count)
#     return count
#
# num = 1
# mySqrt(num)

# Climbing stair(Task 70)
# def climbStairs(n: int) -> int:
#     if n == 1 or n == 2:
#         return n
#     else:
#         i, j, step = 1, 2, 0
#         for _ in range(3, n + 1):
#             step = i + j
#             i = j
#             j = step
#         return step
#
# num = 15
# print(climbStairs(num))

# Merge Sorted Array (Task 88)
# def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#
#     del nums1[m:]
#     nums1.extend(nums2)
#     nums1.sort()
#
#
# nums1 = [0,0,0,0,0]
# nums2 = [1, 2, 3, 5]
# m = 0
# n = 4
# merge(nums1, m, nums2, n)

# Valid Parentheses(Task 20)
# def isValid(s: str) -> bool:
#     if len(s) % 2 != 0:
#         return False
#     par_dict = {'(': ')', '{': '}', '[': ']'}
#     stack = []
#     for char in s:
#         if char in par_dict.keys():
#             stack.append(char)
#             print(stack)
#         else:
#             if stack == []:
#                 return False
#             open_brac = stack.pop()
#             if char != par_dict[open_brac]:
#                 return False
#     return stack == []
#
# s = "[{}]"
# print(isValid(s))

# Binary Tree inorder Traversal (Task 94)
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         return (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)) if root else []
