/* 题目: 旋转矩阵 https://www.nowcoder.com/study/live/718/1/4
    有一个NxN整数矩阵，请编写一个算法，将矩阵顺时针旋转90度。
    给定一个NxN的矩阵，和矩阵的阶数N,请返回旋转后的NxN矩阵。
    
    解法: 
        1、先转置，再水平镜像；
        2、值交换-两个元素：
            a) python： a,b = b,a
            b) c/c++:   a ^= b;     b ^= a;     a ^= b;   */

#include <vector>

vector<vector<int> > rotateMatrix(vector<vector<int> >& mat, int n) {
        // write code here        
        // transmate
        for(int i=1;i<n;i++)
            for(int j=0;j<i;j++){
                mat[i][j]^=mat[j][i];                
                mat[j][i]^=mat[i][j];
                mat[i][j]^=mat[j][i];
            }
            
        // jingxiang-shuiping    
        /**/
        for(int i=0;i<n;i++)
            for(int j=0;j<n/2;j++){
                mat[i][j] ^= mat[i][n-1-j];                
                mat[i][n-1-j] ^= mat[i][j];
                mat[i][j] ^= mat[i][n-1-j];
            }  
        
        return mat;
    }