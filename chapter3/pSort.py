class Solution(object):
    def __init__(self):
        self.res = []
    def pancakeSort(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A or len(A) == 1:
            return self.res
        self.pSort(A, len(A))
        return self.res
    def pSort(self, A, length):
        if length == 1:
            return
        max_index = 0
        for i in range(length):
            if A[i] > A[max_index]:
                max_index = i
        A = self.reverseA(A, 0, max_index)
        self.res.append(max_index+1)
        A = self.reverseA(A, 0, length - 1)
        self.res.append(length)
        self.pSort(A, length - 1)

    def reverseA(self, A, m, n):
        while m < n:
            A[m], A[n] = A[n], A[m]
            m += 1
            n -= 1
        return A
if __name__ == "__main__":
    Solution().pancakeSort([1,2,3])