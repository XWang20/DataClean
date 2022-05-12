from utils import countEnglishChar
import re
from nltk.tokenize import TweetTokenizer
  
# Create a reference variable for Class TweetTokenizer
tk = TweetTokenizer()

# f = open("new_process/rare_ch_char.txt", encoding='utf-8')
# rare = set(f.read())

f_1 = open("英语字符数比例", "w")
f_2 = open("拉丁字符连续", "w")
f_3 = open("token数", "w")

def FilterPara(para, no_pic):
    '''
    文本过滤
    根据中文字数及比例、长度对句子进行过滤
    '''
    para = para.replace("@USER", "").replace("HTTPURL", "")

    length = len(para)
    if not length:
        return False

    # 过滤英语字符数比例
    if countEnglishChar(para)/length < 0.6:
        f_1.write(para+"\n")
        return False

    # 拉丁字符连续出现46次以上
    if re.search(r"[a-zA-Z]{46, }" ,para):
        f_2.write(para+"\n")
        return False

    token_length = len(tk.tokenize(para))
    if (no_pic and token_length < 5) or (not no_pic and token_length < 9):
        f_3.write(para+"\n")
        return False

    return True
