class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals: return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        x_end = intervals[0][1]
        count = 1
        for interval in intervals:
            start = interval[0]
            if start >= x_end:
                count += 1
                x_end = interval[1]
        count = len(intervals) - count
        return count