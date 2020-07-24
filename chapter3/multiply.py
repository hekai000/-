class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        res = [0] *(m+n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1
                sum = int(res[p2]) + mul
                res[p2] = str(sum%10)
                res[p1] = str(int(res[p1]) + (sum / 10))
        res_str = "".join(res)
        return "0" if res_str == "0"*(m+n) else res_str.lstrip('0')

if __name__ == "__main__":
    print Solution().multiply('123', '456')