from typing import List


class Solution:
    def longestCommonPrefix(self, words: List[str]) -> str:
        prefix = words[0]
        for word in words[1:]:
            while word[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


x = Solution()
print(x.longestCommonPrefix(words=["flower", "flow", "flight"]))
