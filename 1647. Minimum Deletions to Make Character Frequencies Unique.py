# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

# Ввод: s = "aab"
#  Вывод: 0
#  Объяснение: s уже хорошо.
# Ввод: s = "aaabbbcc"
#  Вывод: 2
#  Объяснение: Вы можете удалить две буквы 'b, в результате чего получится правильная строка "aaabcc".
# Другой способ — удалить одну букву «b» и одну «c», в результате чего получится хорошая строка «aaabbc».
# Ввод: s = "ceabaacb"
#  Вывод: 2
#  Объяснение: Вы можете удалить обе буквы 'c, в результате чего получится правильная строка "eabaab".
# Обратите внимание, что нас интересуют только символы, которые все еще находятся в конце строки (т. е. частота 0 игнорируется).

# class Solution:
#     def minDeletions(s: str) -> int:
#         s = ''.join(sorted(s))
#         for i in range(s):
#
#         print(s)
#
# Solution.minDeletions(s ="ceabaacb")

import collections
import string

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        result = 0
        lookup = set()
        for c in string.ascii_lowercase:
            for i in reversed(range(1, count[c]+1)):
                if i not in lookup:
                    lookup.add(i)
                    break
                result += 1
        return result