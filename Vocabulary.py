import string
import re

file = open("D:/pyHomework/venv/test.txt","r",encoding="utf-8")
lines=[]
for i in file:
    lines.append(i);
file.close();
print(1)
new=[]

cop = re.compile("[\u4e00-\u9fa5]") # 匹配不是中文

myRe = re.compile(r'(\[.+?\])(.+?)')# 匹配音标
myRe1=re.compile(r'\^[a-z]+.') #匹配^xx.
myRe2=re.compile(r'[^a-zA-Z0-9 ]') #匹配^xx.
for line in lines:
    """
        例子
        impressionist [ɪm’preʃənɪst] n. 印象派画家fluctuant [’flʌktjʊənt] adj. 变动的；波动的slump [slʌmp] n.  下降，衰落
        deliver [dɪ’lɪvə] vt. 递送；传送confidence [’kɒnfɪd(ə)ns] n. 自信victory [’vɪkt(ə)ri] n. 胜利；成功
    """
    line = cop.sub('',line)# 去掉中文
    """
        例子
        impressionist [ɪm’preʃənɪst] n. fluctuant [’flʌktjʊənt] adj. slump [slʌmp] n.  
        deliver [dɪ’lɪvə] vt. ；confidence [’kɒnfɪd(ə)ns] n. victory [’vɪkt(ə)ri] n. ；
    """
    line = myRe.sub('^',line)# 去掉英标，替换成^x.
    """
       例子
       impressionist ^ n. fluctuant ^ adj. slump ^ n.  
       deliver ^ vt. ；confidence ^ n. victory ^ n. ；
    """
    #这里是方便等一下直接查找^xx.替换成某个单一字符。 不能直接把^后面都去掉，因为还有字母，所以需要^x.替换成…^
    line = myRe1.sub('^',line)
    """
       例子
       impressionist ^ fluctuant ^ slump ^  
       deliver ^ ；confidence ^ victory ^ ；
    """
    #可以就可以把非字母非数字的都去掉
    line = myRe2.sub('\r',line)
    """
       例子
       impressionist 
        fluctuant 
         slump 
           
       deliver 
       
       confidence 
        victory 
        
        
    """
    new.append(line)


file_write=open("D:/pyHomework/venv/test2.txt","w",encoding="utf-8")
for var in new:
    if var!='\r' and var != '\n':
        file_write.writelines(var)
file_write.close()
print(2)
