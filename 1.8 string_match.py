#  完整字符串1（括号字符串的有效性） https://www.nowcoder.com/study/live/718/1/8
''' 题目:
        需求: 给定一个字符串str，判断是不是整体有效的括号字符串
            (整体有效：即存在一种括号匹配方案，使每个括号字符均能找到对应的反向括号，
            且字符串中不包含非括号字符)。

        输入描述:
            输入包含一行，代表str
               
        输出描述:
            输出一行，如果str是整体有效的括号字符串，请输出“YES”，否则输出“NO”。

        例如:   IN:     (())     OUT:    YES     
                IN:     ()a()    OUT:    NO      

    解法:
        1、用栈操作：  1)  '(' --> t(入栈);
                      2)  ')' and t[-1]=='(' ： t.pop() (出栈)
                          ')' and t[-1]！='('：  --> t.append(e);

        2、括号计数：'(' --> ++  ')'--> --
                cnt == 0 -->YES    cnt==是其他
    ''' 

def isALLKuoHao(s):
    #s=input().split()
    t=[s[0]]
    for e in s[1:]:
        if e != ')' and e != '(':
            t.append(e)
            break
        elif e=='(':
            t.append(e)
        elif e == ')' and len(t)>0 and t[-1] == '(':
            t.pop()
        else:
            t.append(e)

    if len(t)>0:
        print('NO')
    else:
        print('YES')    

def isALLKuoHao_count(s):
    #s=input()[0]
    
    cnt=0
    for e in s:
        if e=='(':      cnt += 1
        else:        cnt-=1
        if cnt<0: 
            print('NO')
            return 
    if cnt==0:
        print('YES')
    else:
        print('NO')

def isALLKuoHao_in():
    s=input()
    t=[s[0]]
    for e in s[1:]:
        if e != ')' and e != '(':
            t.append(e)
            break
        elif e=='(':
            t.append(e)
        elif e == ')' and len(t)>0 and t[-1] == '(':
            t.pop()
        else:
            t.append(e)

    if len(t)>0:
        print('NO')
    else:
        print('YES')  


if __name__=='__main__':
    # ALLKuoHao_in()

    sa=['()()',
        '()a()']
    for s in sa:
        print(s,end=', ')
        isALLKuoHao_count(s)