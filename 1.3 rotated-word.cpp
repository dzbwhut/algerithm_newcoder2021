/* 题目： 旋转词:  https://www.nowcoder.com/study/live/718/1/2
# 如果一个字符串为str，把字符串的前面任意部分挪到后面形成的字符串叫str的旋转词。
# 如: str=“12345”，str的旋转串有“12345”、“45123”等等。
# 给定两个字符串，判断是否为旋转词。

# 解法:
#     1、sm的用首字母，将sn分两段，分别比较；似乎有bug；
#     2、sm 是否为sn+sn的子串: sm C= sn+sn
*/
#include <windows.h>
#include <bits/stdc++.h>

using namespace std;

int main(void){
    int n,m;
    string sn,sm;
    cin>>n>>m;
    cin>>sn>>sm;
    
    if(sn.size() != sm.size() )
        cout<<"NO";
         
    sn+=sn;    
        
    if(sn.find(sm)==string::npos)
        cout<<"NO";
    else 
        cout<<"YES";   
}