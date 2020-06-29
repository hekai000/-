class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points: return 0
        points = sorted(points, key=lambda x: x[1])
        count = 1
        x_end = points[0][1]
        for point in points:
            start = point[0]
            if start > x_end:
                count += 1
                x_end = point[1]
        return count