class Solution(object):
    def areSimilar(self, mat, k):
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    new_j = (j - k) % n
                else:
                    new_j = (j + k) % n

                if mat[i][j] != mat[i][new_j]:
                    return False

        return True