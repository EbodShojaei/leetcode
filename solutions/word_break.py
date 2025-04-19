from typing import List

# see https://leetcode.com/problems/word-break/


class Solution:
    def wordBreak(s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = [False for _ in range(n + 1)]
        words[0] = True

        for max in range(1, n + 1):
            for min in range(n):
                word = s[min:max]
                if words[min] and word in wordDict:
                    words[max] = True
                    print(word)

        return words[n]


word_dict = ["cats", "dog", "sand", "and", "cat"]
s = "catsandog"

# word_dict = ["apple","pen"]
# s = "applepenapple"

Solution.wordBreak(s, word_dict)
