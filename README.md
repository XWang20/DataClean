# 数据清洗脚本
## 英语数据清洗说明
### 文件说明
* [requirements.txt](requirements.txt) 包中包含了所需要的依赖，使用以下命令安装依赖。
```
$ pip install -r requirements
```
* [clean_data.py](clean_data.py)为数据清洗。包括了以下函数：
    * English_Operate(str)
        * 对英语文本做清洗
    * CleanSent(str):
        * 数据清洗函数
        * 去掉段首尾换行、空格。
        * 去掉标点重复、括号紧跟标点、括号内为空。
        * HTML网址转换和username转换。
        * html_entities 转译（例如lt;）。
    * ReplaceNotation(str)
        * 替换特殊字符以及删除不可见字符函数
        * 字符替换，根据[change.txt](change.txt)表中的字符进行替换。
        * 删除控制字符。
    * SingleProcess(json)
        * 处理一个json的示例
    * MultiProcess(json_list, num_proc)
        * 一个多进程的示例
* [filter_data.py](filter_data.py)为数据过滤。输入为`str`文本。如果需要过滤，则返回False；如果不需要过滤，则返回True。文件中包括了以下过滤方法：
    * 空字符
    * 拉丁字母比例<0.6
    * 没有图片时，token数<5，或有1张图片时，token数<9，或2张图片以上。
* [utils.py](utils.py)给出了一些使用的工具，包括判断是否为英语字母、是否是中文字符等。
* [change.txt](change.txt)文件中是用于字符替换的字表。
* [processor_example.py](processor_example.py)和[multi_process_example.sh](multi_process_example.sh)给出了一个多进程代码使用的示例。

### 使用方法
1. 修改[clean_data.py](clean_data.py)中SingleProcess函数。函数输入为一个json格式的数据，调用Opereate函数清洗需要处理的文本，调用FilterPara函数过滤文本。
2. 按照数据具体情况自定义[clean_data.py](clean_data.py)和[filter_data.py](filter_data.py)。
3. 修改[processor_example.py](processor_example.py)，批量处理json格式的数据。
4. 修改[multi_process_example.sh](multi_process_example.sh)，使用多进程

ps：给出了两种调用多进程的方式：[clean_data.py](clean_data.py)中MultiProcess函数和[multi_process_example.sh](multi_process_example.sh)。可以自主选择合适的方式使用多进程。