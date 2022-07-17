from typing import List, Optional


class Solution:
    # Success
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        toPaint = image[sr][sc]
        return self.fill(image, sr, sc, color, toPaint)

    def fill(self, image, sr, sc, color: int, toPaint: Optional[int]):
        M, N = len(image), len(image[0])

        image[sr][sc] = color

        if sr + 1 < M and image[sr+1][sc] == toPaint and image[sr+1][sc] != color:
            self.fill(image, sr + 1, sc, color, toPaint)
        if sr - 1 >= 0 and image[sr - 1][sc] == toPaint and image[sr - 1][sc] != color:
            self.fill(image, sr - 1, sc, color, toPaint)
        if sc + 1 < N and image[sr][sc + 1] == toPaint and image[sr][sc + 1] != color:
            self.fill(image, sr, sc + 1, color, toPaint)
        if sc - 1 >= 0 and image[sr][sc - 1] == toPaint and image[sr][sc - 1] != color:
            self.fill(image, sr, sc - 1, color, toPaint)

        return image
