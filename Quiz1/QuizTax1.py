import csv
import deepcut
import pandas as pd

from pythainlp.tag import pos_tag_sents
from pythainlp.tag import pos_tag


def Opencsv(opens):
    with open(f'./FileCSV1/{opens}_clean_translated.csv', encoding="utf8") as csvfile:

        reader = csv.reader(csvfile)
        next(reader, None)
        values = []
        for row in reader:
            list_word = deepcut.tokenize(row[1])
            senten = pos_tag(list_word, corpus='orchid_ud')
            tests = [senten]
            test = str(tests)

            clean = test.replace(", (' ', 'PUNCT'), ", "],[")
            clean2 = clean.replace(" ", "")
            values.append(clean2)

        return values


def Savecsv(filds):

    information = Opencsv(filds)
    with open(f'./ResultQuiz1/{filds}_clean_translated.csv', mode='w', encoding="utf8", newline='') as savecsvfile:

        fieldnames = [filds]
        writer = csv.DictWriter(savecsvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in information:
            writer.writerow({filds: row})
        print("Success in ", filds)


def SaveCSVall():

    dict = {'patong_google': Opencsv('patong_google'), 'patong_trip': Opencsv('patong_trip'),
            'promthep_google': Opencsv('promthep_google'), 'promthep_trip': Opencsv('promthep_trip'),
            'wat_google': Opencsv('wat_google'), 'wat_trip': Opencsv('wat_trip'),
            }

    df = pd.DataFrame(dict)
    df.to_csv(f'./ResultQuiz1/Quiz1.csv', index=False)


def main():

    OpenCSVfile = ["patong_google", "patong_trip",
                   "promthep_google", "promthep_trip", "wat_google", "wat_trip"]
    for filds in OpenCSVfile:
        Savecsv(filds)

    SaveCSVall()


main()
