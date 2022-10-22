#  完整字符串2（括号字符串的有效性） https://www.nowcoder.com/study/live/718/1/9
''' 题目:
        需求: 一个完整的括号字符串定义规则如下:
            1、空字符串是完整的。
            2、如果s是完整的字符串，那么(s)也是完整的。
            3、如果s和t是完整的字符串，将它们连接起来形成的st也是完整的。
            例如，  "(()())", ""和"(())()"是完整的括号字符串，
                    "())(", "()(" 和 ")"是不完整的括号字符串。
                    牛牛有一个括号字符串s,现在需要在其中任意位置尽量少地添加括号,
                    将其转化为一个完整的括号字符串。请问牛牛至少需要添加多少个括号。

        输入描述:
            输入包括一行,一个括号序列s,序列长度length(1 ≤ length ≤ 50).
            s中每个字符都是左括号或者右括号,即'('或者')'.
               
        输出描述:
            输出一个整数,表示最少需要添加的括号数

        例如:   IN:   (()(()      OUT:    2       

    解法:
        1、用栈操作：  1)  '(' --> t(入栈);
                      2)  ')' and t[-1]=='(' ： t.pop() (出栈)
                          ')' and t[-1]！='('：  --> t.append(e);

        2、括号计数：'(' --> ++  ')'--> --
                遍历： if cnt == -1:  need++
                遍历完：  need += cnt

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

    print(len(t))


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
    print(len(t))
    
          
if __name__=='__main__':
    isALLKuoHao_in()

    sa=['(()(()',
        '())()']
    for s in sa:
        print(s,end=', ')
        isALLKuoHao(s)