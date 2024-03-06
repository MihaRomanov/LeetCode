# https://leetcode.com/problems/merge-two-sorted-lists/


# list1 = [1,2,4], list2 = [1,3,4]

class Solution:
    result =[]
    def mergeTwoLists(self, list1, list2,result):
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] < list2[j]:
                    result.append(list1[i])
                    

