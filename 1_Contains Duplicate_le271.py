# problem: https://leetcode.com/problems/contains-duplicate/description/

#problem
'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''
#examples
'''
Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true
'''
#solution_1
'''
brute force double for loop
count occurrence
'''
nums = [1,1,1,3,3,4,3,2,4,2]

def solution_1(nums):
    for i in nums:
        count = 0
        for j in nums:

            if j ==i:
                count+=1
        if count >1:
            return True
    return False


#solution-2
'''
sort  and check if two conscutive elements are same
we use sorted
sorted(nums) -> O(n log n)

'''
def solution_2(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False
    
#best solution 
'''
hashset each of them
o(n)
o(n)
'''
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

'''
convert to set and compare len
'''
def containsDuplicate_2(nums):
    return len(nums) != len(set(nums))