#  数轴覆盖 https://www.nowcoder.com/study/live/718/1/6
''' 题目:
        需求: 数轴上有 N 个点，求一条长度为 K 的线段最多覆盖多少个点？
              此处我们认为长度为1的线段最多可以覆盖1个点

        输入描述:
            第一行N和K，表示点数和线段长度
            第二行N个数，表示N个点的坐标
            例如:   
        输出描述:
            输出一个数，最多覆盖的点数
        例如:   IN:     5 3
                        1 3 5 7 9
                OUT:    2
    
    '''
    
st=input().split()
N,K=int(st[0]),int(st[1])
st=input().split()
lt=[int(e) for e in st]

m=1  # 覆盖的最多点数
l=0  # 左边下标

for r in range(1,N):
    if lt[r]-lt[l]<K:#        
        if r-l+1>m:
            m=r-l+1
    else:
        l+=1
    
print(m)    