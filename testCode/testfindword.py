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
            replaceWord = words.replace("\\u200b", "").replace(
                "\\n", "").replace("-ADJ", "").replace("-ADV", "")
            lambdas.append(replaceWord)

    return lambdas


def deepcuts(datas):
    list_word = []

    for word in datas:
        word_cut = deepcut.tokenize(word)
        list_word.append(word_cut)

    numpy_join = np.concatenate(list_word)
    return list(numpy_join)


def keepfile(data, listword):

    for y in data:
        filter_object = filter(lambda a: listword in a, data)
        a = list(filter_object)
        return a


def Stopwords(listword):
    stopword = readcsv('stopword')
    test = list(set(listword) - set(stopword))
    return test


def Pos(data):
    pos = pos_tag(data, corpus='orchid_ud')
    return pos


def FindSentens(partOfSpeech, sentench):

    for y in partOfSpeech:
        filter_object = filter(lambda a: sentench in a, partOfSpeech)
        a = list(filter_object)
    strword = str(a).replace("(", "").replace(" ", "").replace("'", "").replace(",", "")\
        .replace("NOUN", "|").replace("[", "").replace("]", "").replace(")", "")\
        .replace("VERB", "|").replace("ADJ", "|").replace("ADV", "|")
    data = strword.split('|')
    return data


# data = readcsv('WhitespacePOS1')

information = {}
verbs = ['NOUN', 'VERB', 'ADJ', 'ADV']
posnegs = ['POS', 'NEG']

for posneg in posnegs:

    data = readcsv('Whitespace'+posneg)
    listword = deepcuts(data)
    stopword = Stopwords(listword)
    partOfSpeech = Pos(stopword)

    for verb in verbs:
        filds = posneg+verb
        max = len(data)
        bar = IncrementalBar(f'stopword {posneg}_{verb}', max=max,
                             suffix='%(percent)d%% %(elapsed_td)s')
        information[filds] = []
        findword = FindSentens(partOfSpeech, verb)
        for word in findword:
            bar.next()
            if word != "":

                checkid_word = keepfile(data, word)
                if len(checkid_word) >= 2:
                    information[filds].append({'word':word,\
                                               'sentence':checkid_word})

        bar.finish()
        with open(f'./testCode/json/Postgards.json', 'w', encoding='utf8') as outfile:
              json.dump(information, outfile, ensure_ascii=False )



def main():
    data = {}
    counts = 0
    namecsv = ['NOUN']
    name = 'testEachword'
    for readname in namecsv:
        lambdas = readcsv(name+readname)
        max = len(lambdas)
        bar = IncrementalBar(f'Word segment file {readname}', max=max,
                             suffix='%(percent)d%% %(elapsed_td)s')
    #  fileds = 'texts'
        data[readname] = []
        for looplamda in lambdas:
            sentens = keepfile(looplamda)
            bar.next()
            if sentens != []:

                data[readname].append({
                    looplamda: sentens
                })

                counts += 1
            else:
                counts = counts
        bar.finish()

    return data
    # with open(f'./testCode/json/UniquewordDeepcutWordADJADVNOUNVERB1.json', 'w', encoding='utf8') as outfile:
    #     json.dump(data, outfile, ensure_ascii=False )


def unique(splits):
    x = np.array(splits)
    return (np.unique(x))


def save():
    test = main()
    print(test)
    df = pd.DataFrame(test)
    df.to_csv(
        f'/testCode/json/UniquewordDeepcutWordADJADVNOUNVERB1.csv', index=False)


# save()
