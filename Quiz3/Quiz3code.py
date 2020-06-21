import tltk
import csv
import pandas as pd

def Opencsv(opens):
  with open(f'./FileCSV1/{opens}_clean_translated.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    data = []

    next(reader, None)

    print("Procesing in pos_tag > ",opens)

    for row in reader:
        words=row[1]
        word= tltk.nlp.pos_tag(words) 

        Replacestr=str(word)
        Change1 = Replacestr.replace(", ('<s/>', 'PUNCT')","")
        Change2 = Change1.replace(" ","")

        data.append(Change2)

    return data
    
def Savecsv(filds):

    information = Opencsv(filds)
    with open(f'./ResultQuiz3/{filds}_clean_translated.csv', mode='w', encoding="utf8", newline='') as savecsvfile:

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
    df.to_csv(f'./ResultQuiz3/Quiz3.csv', index=False)

    print("Success save all csv file")

def main():

    OpenCSVfile = ["patong_google", "patong_trip",
                   "promthep_google", "promthep_trip",
                    "wat_google", "wat_trip"]
    for filds in OpenCSVfile:
        Savecsv(filds)

    SaveCSVall()


main()
