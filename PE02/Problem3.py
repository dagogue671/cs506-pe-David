"""
Problem 3. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1: Input: ["flower","flow","flight"] Output: "fl"
Example 2: Input: ["dog","racecar","car"] Output: ""
Explanation: There is no common prefix among the input strings.
Note: All given inputs are in lowercase letters a-z.
"""


def longest_common_prefix(array):
    
    ans=""
    str = array[:]
    str = sorted(str)

    first = str[0]
    last = str[-1]

    
    for i in range(min(len(first), len(last))):
        if(first[i] != last[i]): 
            return ans  # Return empty if the first and last string doesn't equal
        ans+=first[i]   # Add character from first list otherwise
    return ans
