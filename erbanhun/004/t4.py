#-*- coding utf-8 -*-

def  dealFile(filename):
    fo = open(filename)
    all_text = fo.read()
    char_chaifen = all_text.split(' ')
    length = len(char_chaifen)

    fo.close()

    return length


if __name__ == '__main__':
    filename = input('ENTER filename : ')
    wordNum = dealFile('t4.txt')
    print(wordNum)
