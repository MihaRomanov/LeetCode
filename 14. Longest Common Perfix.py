#https://leetcode.com/problems/longest-common-prefix/description/

# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longestCommonPrefix(a):
    size = len(a)

    if (size == 0):
        return ""
    if (size == 1):
        return a[0]
    a.sort()
    end = min(len(a[0]), len(a[size - 1]))
    i = 0
    while (i < end and
           a[0][i] == a[size - 1][i]):
        i += 1

    pre = a[0][0: i]
    return pre


# Driver Code
# if __name__ == "__main__":
input = ["geeksforgeeks", "geeks",
             "geek", "geezer"]
print("The longest Common Prefix is :",
          longestCommonPrefix(input))