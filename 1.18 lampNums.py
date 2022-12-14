'''安置路灯：
  题目:
    小Q正在给一条长度为n的道路设计路灯安置方案。
    为了让问题更简单,小Q把道路视为个方格,需要照亮的地方用 '.' 表示, 
    不需要照亮的格子用 'X' 表示。
    小Q现在要在道路上设置一些路灯, 对于安置在 位置的路灯, 
    这盏路灯可以照亮这三个位置。
    但是有个限制，不需要照亮的格子上面不能放置路灯。
    小Q希望能安置尽量少的路灯照亮所有 '.' 区域, 
    希望你能帮他计算一下最少需要多少盏路灯。

    输入描述:  第一行一个正整数n 
          第二行为一个长度为n的字符串，仅由'.'和'X'这两种字符组成。
        数据范围：1≤n≤100000 
    
    输出描述:  最少需要放置的路灯数量
    示例1
        输入: 5
            .X.X. 
        输出: 3 
        说明: 由于不需要照亮的格子上面不能放置路灯，所以必须在1,3,5这三个位置放置路灯  
    示例2 
        输入    5
            ..... 
        输出    2 
        说明    在2,4这两个位置放置路灯即可。
  题解：
    f(i)--i位左侧已亮，判断i位及右侧的情况：
    1）x--直接跳过，f(i+1)；
    2）.--看下一位：
        a) x --> i位加1灯，跳2位；1+f(i+2)
        b） . --> i+1位加1灯，跳3位；1+f(i+3)
    '''

import sys


def getNum(st):
    m = 0  #灯数
    j = 0  #列表浏览计数器
    while j < len(st):  # 不适合用for j in st， 循环体内j值，不能修改
        if st[j] == 'X':
            j += 1
            continue

        m += 1

        if j + 1 < len(st):  # j j+1  j+2  j+3
            if st[j + 1] == 'X':  #  . x
                j += 2
            else:  #  . ./L ./x
                j += 3  #          |
        else:
            break

    return m


st = ['XXX.X.XXXX', '.....', '.X.X.', 'XXXXXXXX.........XX.XXX..X...']
for s in st:
    print(s, ": ", getNum(s))
'''
n=input()
st=input()     
print(getNum(st))
'''
