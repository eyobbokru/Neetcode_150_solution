# problem: https://leetcode.com/problems/valid-anagram/description/

#problem
"""
Given two strings s and t, return true if t is an 
anagram of s, and false otherwise.

 """
#examples
"""
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""
#solution_1
'''
if they have different len return 

if they don't count up for s and down for t
'''

def isAnagram(s: str, t: str) -> bool: 

    if len(s) != len(t):
        return True
    
    counter ={}
    
    #increment for s
    for c in s:
        counter[c] = counter.get(c,0) +1

    #decrement for s
    for ch in t:
        
        if ch not in counter:
            return False
        
        counter[ch] -=1
        if counter[ch] == 0:
            del counter[ch]

    return len(counter) == 0


#solution 
'''
since hashmap is overhead we can do it use array .
we know the letters are fixed len 26
'''


def isAnagram(s: str, t: str) -> bool: 

    if len(s) != len(t):
        return False
    
    count =[0]*26

    for i in range(len(s)):

        count[ord(s[i]) - ord('a')] +=1
        count[ord(t[i]) - ord('a')] +=1

    return not any(count)


#solution_3
'''
we levearge the  count func python str 
'''


def isAnagram(s: str, t: str) -> bool: 

    if len(s) != len(t):
        return False
    
    for char in set(s):
        if s.count(char) != t.count(char):
            return False 
    return True