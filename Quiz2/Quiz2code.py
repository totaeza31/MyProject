import tltk
import csv
import deepcut
import pandas as pd


def Opencsv(opens):

    with open(f'./FileCSV1/{opens}_clean_translated.csv', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        values = []

        print("Procesing in pos_tag > ",opens)

        for row in reader:

            list_word = deepcut.tokenize(row[1])
            test = str(list_word)
            clean = test.replace("'", "")
            clean2 = clean.replace(" ", "")
            clean3 = clean2.replace(",,", ",")


            i = tltk.nlp.pos_tag(clean3)

            test2 = str(i)

            clean3 = test2.replace("(',', 'PUNCT'),", "")
            clean4 = clean3.replace(", ('<s/>', 'PUNCT')", "")
            clean5 = clean4.replace("('[', 'SYM'),", "")
            clean6 = clean5.replace(", (']', 'SYM')", "")
            clean7 = clean6.replace("  ", "")
            clean8 = clean7.replace(", (',.]', 'ADV'),","")
            values.append(clean8)
        return values


def Savecsv(filds):

    information = Opencsv(filds)
    with open(f'./ResultQuiz11/{filds}_clean_translated.csv', mode='w', encoding="utf8", newline='') as savecsvfile:

        fieldnames = [filds]
        writer = csv.DictWriter(savecsvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in information:
            writer.writerow({filds: row})
        print("Success save csv in ", filds)


def SaveCSVall():

    dict = {'patong_google': Opencsv('patong_google'), 'patong_trip': Opencsv('patong_trip'),
            'promthep_google': Opencsv('promthep_google'), 'promthep_trip': Opencsv('promthep_trip'),
            'wat_google': Opencsv('wat_google'), 'wat_trip': Opencsv('wat_trip'),
            }

    df = pd.DataFrame(dict)
    df.to_csv(f'./ResultQuiz11/Quiz2.csv', index=False)

    print("Success save all csv file")

def main():

    OpenCSVfile = ["patong_google", "patong_trip",
                   "promthep_google", "promthep_trip",
                    "wat_google", "wat_trip"]
    for filds in OpenCSVfile:
        Savecsv(filds)

    SaveCSVall()


main()
