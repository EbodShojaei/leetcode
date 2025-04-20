# see https://leetcode.com/problems/longest-substring-without-repeating-characters/

# O(N) solution
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        n = len(s)
        start = 0
        current_length = 0
        max_length = 0
        word = set()
        result = ""
        for end in range(n):
            c = s[end]
            while c in word:
                word.remove(s[start])
                start += 1

            word.add(c)
            current_length = end - start + 1
            if current_length > max_length:
                max_length = current_length
                result = s[start:end+1]

        print(result)
        print(max_length)
        return max_length


# O(N^2) solution
# class Solution:
#     def lengthOfLongestSubstring(s: str) -> int:
#         n = len(s)
#         result = ""
#         for min in range(n):
#             word = []
#             for max in range(min, n):
#                 c = s[max]
#                 if c in word:
#                     break
                
#                 word += c
        
#             if len(word) > len(result):
#                 result = word

#         print("".join(result))
#         print(len(result))
#         return len(result)


# s = "abcabcbb"
# s = "bbbbb"
s = "pwwkew"
# s = " "

Solution.lengthOfLongestSubstring(s)
