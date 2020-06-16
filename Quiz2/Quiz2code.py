import tltk
import csv  
import deepcut

def opencsv(opens):

 with open(f'./FileCSV1/{opens}_clean_translated.csv', encoding="utf8") as csvfile:
     Readpromthep = csv.reader(csvfile)
     values= []
     for row in Readpromthep:
        
        list_word = deepcut.tokenize(row[1]) 
        test= str(list_word)
        clean = test.replace("'","")
        clean2 = clean.replace(" ","")
        clean3= clean2.replace(",,",",")
       
        i=tltk.nlp.pos_tag(clean3)

        test2 = str(i)
        print(test2)
        clean3 = test2.replace("(',', 'PUNCT'),","") 
        clean4 = clean3.replace(", ('<s/>', 'PUNCT')","")
        clean5 = clean4.replace("('[', 'SYM'),","") 
        clean6 = clean5.replace(", (']', 'SYM')","")
        clean7 = clean6.replace("  ","")
        values.append(clean7) 
     return values   
    
def savecsv():
   
    OpenCSVfile=["patong_google","patong_trip","promthep_google","promthep_trip","wat_google","wat_trip"]
   
    for opens in OpenCSVfile:
     information= opencsv(opens)
     with open(f'./ResultQuiz2/{opens}.csv', mode='w',encoding="utf8",newline='') as savecsvfile:

      fieldnames = [opens]
      writer = csv.DictWriter(savecsvfile,fieldnames=fieldnames)
      writer.writeheader()
      for row in information :
          writer.writerow({opens:row})

def main():
  savecsv()
  
main()