# with open("simple_ch_char.txt") as f:
#     SIM_CH_CHAR = set(f.read().strip())
# with open("trad_ch_char.txt") as f:
#     TRA_CH_CHAR = set(f.read().strip())

def isJapaneseChar(char):
    '''
    判断一个字符是否为日语
    '''
    if '\u3040' <= char <= '\u30FF' or '\u31F0' <= char <= '\u31FF' or char == '㈰': 
        return True
    return False

def countJapaneseChar(sent):
    '''
    统计一句话的日语数
    '''
    return sum([isJapaneseChar(x) for x in sent])

def countEnglishChar(sent):
    '''
    统计一句话的英语字母数
    '''
    return len([x for x in sent if 'a' <= x <= 'z' or 'A' <= x <='Z'])

def isChineseChar(char):
    '''
    判断一个字符是否为汉字
    '''
    chinese_char = [['\u2F00', '\u2FDF'],
                    ['\u3000', '\u2FDF'],
                    ['\u3400', '\u4DBF'],
                    ['\u4E00', '\u9FFF'],
                    ['\uF900', '\uFAFF'],
                    ['\U00020000', '\U0002A6DF'],
                    ['\U0002A700', '\U0002B73F'],
                    ['\U0002B740', '\U0002B81F'],
                    ['\U0002B820', '\U0002CEAF'],
                    ['\U0002CEB0', '\U0002EBEF'],
                    ['\U0002F800', '\U0002FA1F'],
                    ['\U00030000', '\U0003134F']]

    for line in chinese_char:
        if line[0] <= char <= line[1]:
            return True
    return False

def countChineseChar(sent):
    '''
    统计一句话的汉字数
    '''
    return sum([isChineseChar(x) for x in sent])

def isChineseWord(word):
    for char in word:
        if not isChineseChar(char):
            return False
    return True

def countSimplifiedChar(sent):
    return len([s for s in sent if s in SIM_CH_CHAR])

def countTraditionalChar(sent):
    return len([s for s in sent if s in TRA_CH_CHAR])

def isTitleCorrect(str):
    if str.startswith("###### ") or str.startswith("##### ") or str.startswith("#### ") or str.startswith("### ") or str.startswith("## ") or str.startswith("# "):
        return True
    return False

def correctTitle(str):
    if str.startswith("#") and not isTitleCorrect(str):
        if str.startswith("######"):
            str = str.replace("######", "###### ")
        elif str.startswith("#####"):
            str = str.replace("#####", "##### ")
        elif str.startswith("####"):
            str = str.replace("####", "#### ")
        elif str.startswith("###"):
            str = str.replace("###", "### ")
        elif str.startswith("##"):
            str = str.replace("##", "## ")
        elif str.startswith("#"):
            str = str.replace("#", "# ")
    return str
