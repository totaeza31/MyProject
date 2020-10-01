import numpy as np
import csv
import pandas as pd

# function to get unique values


def unique(splits):
    x = np.array(splits)
    unqies = np.unique(x)
    return unqies


def readcsv(filds, posneglop):
    with open(f'./testCode/csv/{filds}.csv', encoding="utf8") as csvfile:
        readers = csv.reader(csvfile)
        data = []
        next(readers, None)
        for row in readers:
            words = row[2]
            posneg = row[3]
            if posneg == posneglop:
                data.append(words)
            #    name=words.split()
        return data


def Splitword(data):
    strinformation = str(data)
    replacestrinformation = strinformation.replace("'", '')\
                                          .replace('[', '')\
                                          .replace(']', '')\
                                          .replace('\"', '')\
                                          .replace('.', '')\
                                          .replace(',', ' ')
    splits = replacestrinformation.split()
    return splits


def main1():

    dataname = ["POS", "NEG"]
    for loop_dataname in dataname:
        data = readcsv('data', loop_dataname)
        splits = Splitword(data)

        information = []

        for countSplits in splits:
            if len(countSplits) >= 15:
                information.append(countSplits)
        cutsenten = unique(information)

        dict = {'words': cutsenten}
        df = pd.DataFrame(dict)
        df.to_csv(f'./testCode/csv/Whitespace{loop_dataname}.csv', index=False)


main1()
