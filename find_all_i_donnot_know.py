#!python2
#coding:utf-8
import os
import re
import msvcrt
# number_of_all_words = 0
list_of_new_words = []
list_of_I_know = []
def real_word(word):
    p = re.compile('[a-z,A-Z,\',‘]')
    a = p.findall(word)
    str = ''
    real_word = str.join(a)
    return real_word.lower()

def split_the_article(article):
    number_of_all_words = 0
    list_of_words = []
    paragraphs = article.split('\n')
    for each_filct in paragraphs:
        lines_1 = each_filct.split('.')
        for each_filct in lines_1:
            lines_2 = each_filct.split(',')
            for each_filct in lines_2:
                words = each_filct.split(' ')
                for each_filct in words:
                    each_filct = real_word(each_filct)
                    if each_filct not in list_of_words:
                        number_of_all_words+=1
                        list_of_words.append(each_filct)
    return list_of_words,number_of_all_words

def read(path,name):
    global list_of_I_know,list_of_new_words
    with open(path)as f:
        article = f.read()
    words,num = split_the_article(article)
    print 'there are '+str(num)+' words in '+name
    num = 0
    for each_filct in words:
        if each_filct not in list_of_I_know:
            num +=1
            list_of_new_words.append(each_filct)
    if num == 0:
        print 'No new word'
    elif num ==1:
        print 'only 1 new word'
    else:
        print str(num)+' of them are new words'
    f.close()
    return num

def get_name(path):
    try:
        names = os.listdir(path)
    except:
        os.mkdir('../articles/')
        names = os.listdir(path)
    return names

def Read_what_I_know():
    global list_of_new_words,list_of_I_know
    try:
        with open ('../old.txt')as f:
            all_the_words = f.read()
    except:
        print '\'old.txt\' missing......'
        f = open('old.txt','w')
        f.close
        print '\'old.txt\'created!'
        with open ('./old.txt')as f:
            all_the_words = f.read()
    list_of_I_know,num = split_the_article(all_the_words)
    print 'There are ' + str(num)+' words I have known'
    f.close()

def my_input(output):
    try:
        judge = input(output)
    except:
        print 'Input error! Plz try again:'
        judge = my_input(output)
    return judge

def learn(num):
    real_new_words = []
    num_new = 0
    global list_of_I_know,list_of_new_words
    print 'if you know the word print 1, else print 2'
    for each_filct in list_of_new_words:
        num -=1
        judge = my_input(each_filct+'('+str(num)+' Left)\n')
        if judge == 1:
            list_of_I_know.append(each_filct)
        else:
            real_new_words.append(each_filct)
            num_new +=1
    old = open('../old.txt','w')
    for each_filct in list_of_I_know:
        old.write(each_filct+' ')
    old.close()
    return real_new_words,num_new

def write_each_new_words(name):
    try:
        f = open('../new_words_of_each_article/'+name,'w')
        return f
    except:
        print 'failed to creat file of \'./new_words_of_each_article/'+name+'\''
        print 'creating dir \'./new_words_of_each_article/\''
        try:
            os.mkdir('../new_words_of_each_article/')
            print 'creating file of \'./new_words_of_each_article/'+name+'\''
            try:
                f = open('../new_words_of_each_article/'+name+'','w')
                return f
            except:
                print 'failed to creat file of \'./new_words_of_each_article/'+name+'\'again! I give up~'
        except:
            print 'creating dir \'./new_words_of_each_article/\' failed!'

if __name__ =='__main__':
    flag = 3
    if flag != 1 and flag !=2:
        flag = input('print 1 to build model\nprint 2 to find model\nhere to get some help:https://zhuanlan.zhihu.com/p/25003457\n')
    new_word_all = []
    Read_what_I_know()
    path = r'../articles'
    file_names = get_name(path)
    print file_names
    for each_filct in file_names:
        print 'opening' + each_filct + '......'
        path_1 = path + '/' + each_filct
        num = read(path_1,each_filct)
        if not num == 0:
            if flag == 1:
                real_new_words,num_new = learn(num)
                if not num_new == 0:
                    print 'new words:'
                    print real_new_words
                    f = write_each_new_words(each_filct)
                    for each_filct in real_new_words:
                        new_word_all.append(each_filct)
                        f.write(each_filct)
            else:
                for each_filct in list_of_new_words:
                        new_word_all.append(each_filct)
            list_of_new_words = []
    new = open('../new.txt','w')
    for each_filct in new_word_all:
        new.write(each_filct+'\n')
    new.close()
    print ord(msvcrt.getch())