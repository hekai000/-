# -*-coding: utf-8 -*-
#双向BFS
class Solution(object):
    def plusOne(self, s, pos):
        if s[pos] == '9':
            t = s[:pos] + "0" + s[pos+1:]
        else:
            t = s[:pos] + str((int(s[pos]) + 1)) + s[pos+1:]
        return t
    def minusOne(self, s, pos):
        if s[pos] == '0':
            t = s[:pos] + "9" + s[pos+1:]
        else:
            t = s[:pos] + str((int(s[pos]) - 1)) + s[pos+1:]
        return t

    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        visited = set()
        q1 = set()
        q2 = set()
        if "0000" in deadends:
            return -1
        for i in deadends:
            visited.add(i)
        q1.add("0000")
        q2.add(target)
        step = 0
        while q1 and q2:
            temp = set()
            for cur in q1:
                if cur in visited:
                    continue
                if cur in q2:
                    return step
                visited.add(cur)
                for j in range(4):
                    up = self.plusOne(cur, j)
                    down = self.minusOne(cur, j)
                    if up not in visited:
                        temp.add(up)
                    if down not in visited:
                        temp.add(down)
            step += 1
            q1 = q2
            q2 = temp
        return -1

if __name__ == "__main__":
    print Solution().openLock(["8888"], "1601")