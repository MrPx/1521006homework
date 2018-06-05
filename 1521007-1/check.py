import string
def str(s):
    en=dg=sp=ch=el=0
    for i in s:
        if i>= u'\u4e00'and i<=u'\u9fa5':
            ch+=1
        elif i.isdigit():
            dg+=1
        elif i.isspace():
            sp+=1
        elif i.isalpha():
            en+=1
        else:
            el+=1
    print("英文=%d,数字=%d,空格=%d,中文=%d,其他字符=%d" %(en,dg,sp,ch,el))
