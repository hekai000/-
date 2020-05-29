# -*- coding: utf-8 -*-
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
#
#  示例：
#
#  输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
#
#  说明：
#
#
#  如果 S 中不存这样的子串，则返回空字符串 ""。
#  如果 S 中存在这样的子串，我们保证它是唯一的答案。
#
#  Related Topics 哈希表 双指针 字符串 Sliding Window


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = {}
        window = {}
        for i in t:
            if i not in need:
                need[i] = 1
            else:
                need[i] += 1
        left = 0
        right = 0
        valid = 0
        length = float('inf')
        start = 0
        while right < len(s):
            c = s[right]
            right += 1

            if c in need and need[c]:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1

                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need and need[d]:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return s[start:start+length] if length < float('inf') else ""

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print Solution().minWindow(s, t)