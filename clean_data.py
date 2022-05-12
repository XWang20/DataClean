#encoding:utf-8
'''
英文文本预处理函数，包含
* 过滤：过滤英语比例小、命名实体多、重复字符多的文档。
* 符号去除及转换：替换特殊字符，删除部分不可见字符
* 数据清洗：包含清洗使用错误的标点符号，删除首尾空格等，url、用户名替换等
'''
import re
import functools
import multiprocessing
from tqdm import tqdm

# from utils import isChineseChar, isJapaneseChar
from filter_data import FilterPara
import html

# 建立替换表
with open('change.txt') as f:
    mapping = {}
    for line in f:
        chars = line.strip('\n').split('\t')
        mapping[chars[0]] = chars[1]
    # 替换回车键至换行键
    mapping["\u000D"] = "\u000A"
    mapping["\u2028"] = "\u000A"
    mapping["\u2029"] = "\u000A"
    # 替换\t至空格
    mapping["\u0009"] = "\u0020"

def CleanSent(str):
    '''
    数据清洗
    清洗使用错误的标点符号，删除首尾空格等
    '''

    def repl1(matchobj):
        return matchobj.group(0)[0]
    def repl2(matchobj):
        return matchobj.group(0)[-1]
    
    # 去掉段首尾换行
    str = str.strip()
    # 标点重复
    str=re.sub(r'([（《【‘“\(\<\[\{）》】’”\)\>\]\} ,;:·；：、，。])\1+',repl1,str)
    # 括号紧跟标点
    str=re.sub(r'[（《【‘“\(\<\[\{][ ,.;:；：、，。！？·]',repl1,str)
    str=re.sub(r'[ ,.;:；：、，。！？·][）》】\)\>\]\}]',repl2,str)
    # 括号内为空
    str=re.sub(r'([（《【‘“\(\<\[\{\'\"][\'\"）》】’”\)\>\]\}])','',str)
    # 三个。和.以上的转为...
    str = re.sub(r'[。.]{3,}', '...', str)

    # HTML网址清洗和username清洗
    str = re.sub("(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]", "HTTPURL", str)      # url
    str = re.sub("@\S+", "@USER", str)      # username

    # html_entities 转译
    str = html.unescape(str)

    return str

def ReplaceNotation(str):
    '''
    替换特殊字符以及删除不可见字符
    '''
    
    char_list = list(map(lambda x:mapping.get(x, x), str))
    for id, x in enumerate(char_list):
        # 删除不可见字符 
        if "\u2000" <= x <= "\u200F" or "\u0000" <= x <= "\u001F" and x != "\n":
            char_list[id]=''
    
    # 替换特殊字符
    return ''.join(char_list)

def English_Operate(content):
    content = ReplaceNotation(content)
    content = CleanSent(content)
    return content

def SingleProcess(data_unit):
    # 按照需求改写该部分函数

    post = data_unit['body']
    if post[0].startswith("RT"):
        return None

    no_pic = not data_unit["pic_num"]
    repost = data_unit["meta"]["repost"][0]["text"] if data_unit["meta"]["repost"] else []

    post = [English_Operate(content) for content in post]
    repost = [English_Operate(content) for content in repost]

    if not FilterPara(''.join(post), no_pic):
        return None

    if repost:
        return {"text": post, "repost": repost}

    return {"text": post}

def MultiProcess(data_list, num_proc):
    results = []
    with multiprocessing.Pool(num_proc) as p:
        max_ = len(data_list)
        with tqdm(total=max_, desc='Operating data') as pbar:
            for message in enumerate(p.imap_unordered(functools.partial(SingleProcess), data_list)):
                # 对返还结果做处理
                if message:
                    if "repost" in message.keys():
                        results.append(message)
                pbar.update()
    return results

def main():
    # # 清洗文本
    # import json
    # f = open("/data/private/wangxing/OpenSoCo/original/en/0_1.json")
    # for line in tqdm(f):
    #     SingleProcess(json.loads(line.strip()))
    # # 清洗单个json数据
    # SingleProcess(data_unit)
    pass

if __name__ =="__main__":
    main()
