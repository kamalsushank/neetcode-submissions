class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix)-1
        while l<=r:
            mid = (l+r)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                if matrix[mid][-1] >= target:
                    return target in matrix[mid]
                else:
                    l = mid +1
            else:
                r = mid -1
        return False