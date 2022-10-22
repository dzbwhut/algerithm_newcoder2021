''' 题目: 旋转矩阵 https://www.nowcoder.com/study/live/718/1/4
    有一个NxN整数矩阵，请编写一个算法，将矩阵顺时针旋转90度。
    给定一个NxN的矩阵，和矩阵的阶数N,请返回旋转后的NxN矩阵。

    解法:
        1、先转置，再水平镜像；
        2、值交换-两个元素：
            a) python： a,b = b,a
            b) c/c++:    a ^= b;     b ^= a;     a ^= b;  
                库函数: swap(a,b),  reverse(mat[i].begin(),mat[i].end())
    '''

class Solution:
    #def rotateMatrix(self , mat: List[List[int]], n: int) -> List[List[int]]:
    def rotateMatrix(self , mat, n: int):
        # write code here
        m=int(n/2)
        # transmate
        for i in range(1,n):
            for j in range(i):
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            
        # jingxiang-shuiping    
        for i in range(n):
            for j in range(m):
                mat[i][j],mat[i][n-1-j] = mat[i][n-1-j],mat[i][j]
        '''    '''
                
        return mat

if __name__=='__main__':
    sol=Solution()
    matA=[[1,2,3],[4,5,6],[7,8,9]]
    matB=sol.rotateMatrix(matA,3)
    print(matB)