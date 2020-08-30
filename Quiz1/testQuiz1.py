import csv
import deepcut
import pandas as pd

from pythainlp.tag import pos_tag_sents
from pythainlp.tag import pos_tag


def Opencsv():
    # with open(f'./FileCSV1/{opens}_clean_translated.csv', encoding="utf8") as csvfile:

        # reader = csv.reader(csvfile)
        # next(reader, None)

        values = []
        # for row in reader:
        list_word = deepcut.tokenize("ทดสอบตัวตัดคำ")
        values.append(list_word)
        print(values)
        return values

Opencsv()
