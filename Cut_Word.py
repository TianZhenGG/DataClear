#coding='utf-8'
import csv
import jieba
import pandas as pd


file_ob = open('/home/tianzhen/Desktop/gg.csv').read().split('\n')
Rs2 = []
for i in range(len(file_ob)):
    result = []
    seg_li = jieba.cut(file_ob[i])
    for w in seg_li:
        result.append(w)
    Rs2.append(result)

file = open('/home/tianzhen/Desktop/Rs.txt', 'w');
file.write(str(Rs2));
file.close();

txt = open("/home/tianzhen/Desktop/Rs.txt", encoding="utf-8").read()

stopwords = [line.strip() for line in open("/home/tianzhen/Desktop/go.txt", encoding="utf-8").readlines()]
words = jieba.lcut(txt)
counts = {}
for word in words:
    if word not in stopwords:

        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)

for i in range(1000):
    word, count = items[i]

    #print("{:<5}{:>5}".format(word, count),)

with open("cc.csv", "w", newline="") as datacsv:
    # dialect为打开csv文件的方式，默认是excel，delimiter="\t"参数指写入的时候的分隔符
    csvwriter = csv.writer(datacsv, dialect=("excel"))
    # csv文件插入一行数据，把下面列表中的每一项放入一个单元格（可以用循环插入多行）
    for i in items:
        csvwriter.writerow(i)

