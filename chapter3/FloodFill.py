class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.visited = [[0 for _ in range(len(image[0]))] for _ in range(len(image))]
        origColor = image[sr][sc]
        self.fill(image, sr, sc, origColor, newColor)
        return image
    def fill(self, image, sr, sc, origColor, newColor):
        if not self.isValid(sr, sc, image):
            return
        if image[sr][sc] != origColor: return
        if self.visited[sr][sc]: return
        image[sr][sc] = newColor
        self.visited[sr][sc] = 1

        self.fill(image, sr - 1, sc, origColor, newColor)
        self.fill(image, sr + 1, sc, origColor, newColor)
        self.fill(image, sr, sc - 1, origColor, newColor)
        self.fill(image, sr, sc + 1, origColor, newColor)

        return
    def isValid(self, sr, sc, image):
        return 0 <= sr < len(image) and 0 <= sc < len(image[0])

if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    newColor = 2
    print Solution().floodFill(image, sr, sc, newColor)
