#-*- coding:utf-8-*-
import collections
import re
import os

def calcWordNum(filename, filepath):
    os.chdir(filepath)
    files = open(filename)
    content = files.read()
    content_list = content.split(' ')
    # tally occurences of words in a list
    cnt = collections.Counter()
    for word in content_list:
        cnt[word] += 1

    #print (cnt[word])
    # find the 10 most words in file
    stop_word = ['the', 'in', 'of', 'and', 'to', 'has', 'that', 's',\
            'is', 'are', 'a', 'with', 'as', 'an', 'her', 'by']
    words = re.findall(r'\w+', open(filename).read().lower())
    #print (words)
    run_word = []
    for word  in words:
        flag = 0
        for word_compare in stop_word:
            if word_compare == word:
                flag = 1
        if flag == 0:
            run_word = run_word+[word]
    #print (run_word)
    list_word = collections.Counter(run_word).most_common(7)
    return list_word

if __name__ == "__main__":
    filename = 'daily.txt'
    filepath = 'f:\python'
    word = calcWordNum(filename, filepath)
    print (word)
