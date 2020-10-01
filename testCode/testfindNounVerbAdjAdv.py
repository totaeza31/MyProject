import json
import csv
import deepcut
import pandas as pd
import numpy as np
from progress.bar import IncrementalBar
from pythainlp.tag import pos_tag


def readcsv(filename):

    with open(f'./testCode/csv/{filename}.csv', encoding="utf8") as csvfile:
        readers = csv.reader(csvfile)
        lambdas = []
        next(readers, None)
        for row in readers:
            words = row[0]

            lambdas.append(words)
    return lambdas


def readcsvPOS(filename):

    with open(f'./testCode/csv/{filename}.csv', encoding="utf8") as csvfile:
        readers = csv.reader(csvfile)
        lambdas = []
        next(readers, None)
        for row in readers:
            words = row[0]
            lambdas.append(words)
        data = pos_tag(lambdas, corpus='orchid_ud')
    return data


def FindSentens(looplamda, data):
    ls = data
    for y in ls:
        filter_object = filter(lambda a: looplamda in a, ls)
        a = list(filter_object)
        strword = str(a).replace("(", "").replace(" ", "").replace("'", "").replace(",", "")\
            .replace("NOUN", "|").replace("[", "").replace("]", "").replace(")", "")\
            .replace("VERB", "|").replace("ADJ", "|").replace("ADV", "|")

    data = strword.split('|')
    return data


def keepfile(looplamda):
    ls = readcsv('datafromwithspace1')
    for y in ls:
        filter_object = filter(lambda a: looplamda in a, ls)
        a = list(filter_object)
    return a

def main():

    jsonFile = {}
    data = readcsvPOS('UniquewordDeepcutWordTestset1')
    sentences = ['NOUN', 'VERB', 'ADJ', 'ADV']
    posnegs = ['pos', 'neg']

    for posneg in posnegs:
        for sentence in sentences:
            namefild = posneg+sentence
            jsonFile[namefild] = []
            find = FindSentens(sentence, data)

            for ids in find:
                if ids != '':
                    text = keepfile(ids)
                    jsonFile[namefild].append({"word": ids, "sentence": text})

    with open('./testCode/json/Patong_Beach/UniquewordDeepcutWordTestset.json', 'w', encoding='utf8') as outfile:
        json.dump(jsonFile, outfile, ensure_ascii=False)

def unique(splits):
    x = np.array(splits)
    return (np.unique(x))


main()

#  fileds = 'texts'
#  for looplamda in lambdas:
#   sentens = keepfile(looplamda)
#   bar.next()
#   if sentens != []:
# ranges_sentens = len(sentens)
#    data.append({looplamda:sentens})
#    counts+=1
#   else:
#    counts=counts
#  bar.finish()

#  print(counts)
# สร้าง json แบบ {{name:}{name:}} ใช้ ranges
# for ranges in range(ranges_sentens):
# data[looplamda].append({
# looplamda: sentens[ranges] })
# looplamda: sentens })
