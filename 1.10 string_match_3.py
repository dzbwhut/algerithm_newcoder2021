#  最长合法括号子串 https://www.nowcoder.com/study/live/718/1/10
''' 题目:
        给定一个只包含左右括号的序列，求最长的合法子串满足括号能对应匹配。

        输入描述:
            输入数据一行，只包含'(' 和 ‘)’。 字符串的长度在[1,100000]之间。
               
        输出描述:
            求最长的合法子串。

        例如:   IN:  )()(())((()()    OUT:   6

    解法1: 栈--匹配括号
        1、用栈操作：  1)  '(' --> t(入栈);
                      2)  ')' and t[-1]=='(' ： t.pop() (出栈)
                          ')' and t[-1]！='('：  --> t.append(e);
        2、入栈的是字符串的序号，非匹配的序号的差值，就是各个有效字符串：
            因为匹配的都被消除了
                                       re-1 pre       i-1 i
    解法2: 动态规划--以i结尾的串        ( )   ( (((())) )   )
        1、'(' -- dp[i]=0         dp   0 2             8

        2、')' -- pre = dp[i-1]-1
            pre=='(' -- dp[i]=dp[i-1]+2
              if pre-1>0 -- dp[i]+=dp[pre-1]
    ''' 

def match_sign_len(s):
    #s=input().split()
    p=[] # 2、待配对的括号入栈
    for j,e in enumerate(s):
        if e == '(':
            p.append(j)
        elif e == ')' and len(p)>0 and s[p[-1]] == '(':
            p.pop()
        else:
            p.append(j)

    if len(p)==0:
        return s 
    else:
        m=p[0]
        p.append(len(s))
        for j in range(1,len(p)):
            n=p[j]-1-p[j-1]
            if n>m:
                m=n
        return m 

def match_sign_len_dp(s):    
    if len(s)<2:
        return 0
    
    dp=[0]*len(s)
    ml=0
    for i,c in enumerate(s):
        if c==')':
            pre=i-dp[i-1]-1
            if pre>=0 and s[pre]=='(':
                dp[i]=dp[i-1]+2+ (dp[pre-1] if pre-1>0 else 0)
            ml=dp[i] if dp[i]>ml else ml

    return ml

if __name__=='__main__':   
    # s=input()  
    s=[')(()((((()))))))()()(()(()(())()()()))())(']    
    print(s[0],end=', ')
    print(match_sign_len_dp(s[0]))