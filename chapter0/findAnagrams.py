class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result = []
        need = {}
        window = {}
        for i in p:
            if i not in need:
                need[i] = 1
            else:
                need[i] += 1

        left = 0
        right = 0
        valid = 0
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            while right - left >= len(p):
                if valid == len(need):
                    result.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return result

if __name__ == "__main__":
    s = "baa"
    p = "aa"
    print Solution().findAnagrams(s, p)