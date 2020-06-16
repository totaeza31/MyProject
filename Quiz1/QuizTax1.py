import csv
import deepcut

from pythainlp.tag import pos_tag_sents
from pythainlp.tag import pos_tag

def Opencsv(opens):
    with open(f'./FileCSV1/{opens}_clean_translated.csv', encoding="utf8") as csvfile:
    
     Readpromthep = csv.reader(csvfile)
     values= []
     for row in Readpromthep:
        list_word = deepcut.tokenize(row[1])    
        senten = pos_tag(list_word, corpus='orchid_ud')
        tests =[senten]
        test = str(tests)
      
        clean = test.replace(", (' ', 'PUNCT'), ","],[")
        clean2= clean.replace(" ","")  
        values.append(clean2)

     return values

# patong
def savecsv():

    OpenCSVfile=["patong_google","patong_trip","promthep_google","promthep_trip","wat_google","wat_trip"]
   
    for opens in OpenCSVfile:
      information= Opencsv(opens)
      with open(f'./Quzi1/ResultQuiz1/{opens}_clean_translated.csv', mode='w',encoding="utf8",newline='') as savecsvfile:
 
       fieldnames = [opens]
       writer = csv.DictWriter(savecsvfile,fieldnames=fieldnames)
       writer.writeheader()
       for row in information:
           writer.writerow({opens:row})


def main():
       savecsv()
main()