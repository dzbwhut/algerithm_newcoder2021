# 题目：
# 如果一个字符串为str，把字符串的前面任意部分挪到后面形成的字符串叫str的旋转词。
# 如: str=“12345”，str的旋转串有“12345”、“45123”等等。
# 给定两个字符串，判断是否为旋转词。

# 解法:
#     1、sm的用首字母，将sn分两段，分别比较；似乎有bug；
#     2、sm 是否为sn+sn的子串

# sm1 ?= sn2 && sm2 ?= sn1
def rotated_word_1(sn,sm):
    n,m=len(sn),len(sm)
    if m != n:
        rev= 'NO'
    else:    
        p=sn.index(sm[0])
        #print(f'p: {p} {sn[p:]} ?= {sm[:p]}')
        if p<0:
            rev= 'NO'
        else:
            if p==0:
                if sn==sm:
                    rev= 'YES'
                else:
                    rev= 'NO'
            else:
                if sn[p:]==sm[:n-p] and sn[:p]==sm[n-p:]:
                    rev= 'YES'
                else:
                    rev= 'NO'
    return rev

# sm C= sn+sn
def rotated_word_2(sn,sm):
    n,m=len(sn),len(sm)
    if m != n:
        rev = 'NO'
    else:    
        sn+=sn
        p = sn.index(sm)
        #print(f'p: {p} {sn[p:]} ?= {sm[:p]}')
        if p<0:
            rev= 'NO'
        else:          
            rev= 'YES'

    return rev


if __name__=='__main__':
    #nl=input().split()
    # [n,m]=int(nl[0]),int(nl[1])
    sn= '1234' #input()
    sm= '4123'# input() 
    print(f's1: {sn}, s2: {sm}')
    print(rotated_word_1(sn,sm))
    print(rotated_word_2(sn,sm))
    