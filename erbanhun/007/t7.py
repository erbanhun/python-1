#-*-coding:utf-8-*-
# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。
# 包括空行和注释，但是要分别列出来
import os
import sys
from importlib import reload
reload(sys)

def count(filepath):
    os.chdir(filepath)
    line_cnt = 0
    line0_cnt = 0
    lineNote_cnt = 0
    for filename in os.listdir(filepath):
        print (filename)
        file_object = open(filename) # 含有中文会报错
        #print (file_object)
        file_content = file_object.read()
        #print (file_content)
        content_list = file_content.split('\n')
        line_cnt += len(content_list) - 1

        for line_content in content_list:
            if line_content.strip() == '': # 判断 空行
                line0_cnt += 1
            if line_content.startswith('#') == 1: # 判断 注释行
                lineNote_cnt += 1
        print (line_cnt, line0_cnt, lineNote_cnt)
        file_object.close()
        line0_cnt += -1
    return line_cnt, line0_cnt, lineNote_cnt

if __name__ == '__main__':
    filepath = 'f:\python\code'
    a = count(filepath)
    print (a[0], a[1], a[2])
