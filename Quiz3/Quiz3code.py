import tltk
import csv

def Opencsv(opens):
  with open(f'./FileCSV1/{opens}_clean_translated.csv', encoding="utf8") as csvfile:
    test = csv.reader(csvfile)
    testss= []
    for row in test:
        words=row[1]
        word= tltk.nlp.pos_tag(words) 

        Replacestr=str(word)
        Change1 = Replacestr.replace(", ('<s/>', 'PUNCT')","")
        Change2 = Change1.replace(" ","")
        Change3 = Change2.replace(", ('<s/>', 'PUNCT')","")
        Change4 = Change3.replace("","")
        testss.append(Change4)

    return testss
    
def savecsv():

    OpenCSVfile=["patong_google","patong_trip","promthep_google","promthep_trip","wat_google","wat_trip"]
   
    for opens in OpenCSVfile:
      information= Opencsv(opens)
      with open(f'./ResultQuiz3/{opens}_clean_translated.csv', mode='w',encoding="utf8",newline='') as savecsvfile:
 
       fieldnames = [opens]
       writer = csv.DictWriter(savecsvfile,fieldnames=fieldnames)
       writer.writeheader()
       for row in information:
           writer.writerow({opens:row})
       print("succes ",opens)   

def main():
       savecsv()
main()