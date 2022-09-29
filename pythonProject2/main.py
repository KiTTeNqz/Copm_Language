import nltk
path = "dataset.txt"

from nltk import sent_tokenize
from nltk import word_tokenize
from nltk.corpus import stopwords

def graphematic(text):

    sent=text
    result_list=[]
    stop_words=set(stopwords.words('russian'))
    for word1 in sent:
        tmp=word1
        words=word_tokenize(tmp)
        no_stop_word = [word for word in words if not word in stop_words]
        for word2 in no_stop_word:
            result_list.append(word2)
    wordFreq={}
    for word in result_list:
        if word in wordFreq.keys():
            wordFreq[word]+=1
        else:
            wordFreq[word]=1
    print()
    sortedList = {k: v for k, v in sorted(wordFreq.items(), key=lambda  item: (-item[1], item[0]))}

    for word in sortedList:
        print(word, sortedList[word])
    file.close()

def ex1():
    file = open(path, "r", encoding="utf8")
    text = file.readlines()
    d = 1
    for el in text:
        sentences = sent_tokenize(el)
        for i in range(len(sentences)):
            print(str(d) + ": " + str(sentences[i]))
            d+=1
    file.close()

def ex2():
    d = 1
    file = open(path, "r", encoding="utf8")
    text = file.readlines()
    for el in text:
        sentences = sent_tokenize(el)
        for i in range(len(sentences)):
            sent = sentences[i]
            words = word_tokenize(sent)
            print("Слова из предложения " + str(d) + ":", sep="")
            print(words, sep=" ")
            d += 1
            print("\n")
    file.close()

def ex4():
    print(stopwords.words('russian'))

def ex5():
    file = open(path, "r", encoding="utf8")
    text = file.readlines()
    d = 1
    st_words = set(stopwords.words('russian'))
    for el in text:
        sentences = sent_tokenize(el)
        for i in range(len(sentences)):
             sent = sentences[i]
             words = word_tokenize(sent)
             without_stop_words = [word for word in words if not word in st_words]
             print("Слова из предложения " + str(d) + " без стоп-слов:", sep="")
             print(without_stop_words, sep=" ")
             d += 1
             print("\n")
    file.close()

file = open(path, "r", encoding="utf8")
text = file.readlines()

ex1()
ex2()
ex4()
ex5()
graphematic(text)