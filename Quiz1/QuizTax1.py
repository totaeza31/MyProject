import csv
import deepcut
import pandas 
from pythainlp.tag import pos_tag_sents
from pythainlp.tag import pos_tag
def opencsvPromTrip():
    with open('./FileCSV1/promthep_trip_clean_translated.csv', encoding="utf8") as csvfile:
     Readpromthep = csv.reader(csvfile)
     values= []
     for row in Readpromthep:
        list_word = deepcut.tokenize(row[1])    
        
        senten = pos_tag(list_word, corpus='orchid_ud')

        test = str(senten)
        clean = test.replace(", (' ', 'PUNCT'), ","],[")
      
        sentens=[clean]
        
        values.append(sentens)
     return values

def opencsvPromGoogle():
    with open('./FileCSV1/promthep_google_clean_translated.csv', encoding="utf8") as csvfile:
     Readpromthep = csv.reader(csvfile)
     values= []
     for row in Readpromthep:
        list_word = deepcut.tokenize(row[1])    
        
        senten = pos_tag(list_word, corpus='orchid_ud')

        test = str(senten)
        clean = test.replace(", (' ', 'PUNCT'), ","],[")
      
        sentens=[clean]
        
        values.append(sentens)
     return values

def opencsvPatongGoogle():
    with open('./FileCSV1/patong_google_clean_translated.csv', encoding="utf8") as csvfile:
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


     return  values

def opencsvPatongTrip():
    with open('./FileCSV1/patong_trip_clean_translated.csv', encoding="utf8") as csvfile:
     Readpromthep = csv.reader(csvfile)
     values= []
     for row in Readpromthep:
        list_word = deepcut.tokenize(row[1])    
        
        senten = pos_tag(list_word, corpus='orchid_ud')

        test = str(senten)
        clean = test.replace(", (' ', 'PUNCT'), ","],[")
      
        sentens=[clean]
        
        values.append(sentens)
     return values

def opencsvWatGoogle():
    with open('./FileCSV1/wat_google_clean_translated.csv', encoding="utf8") as csvfile:
     Readpromthep = csv.reader(csvfile)
     
     values= []
     for row in Readpromthep:
        
        list_word = deepcut.tokenize(row[1])    
        
        senten = pos_tag(list_word, corpus='orchid_ud')

        test = str(senten)
        clean = test.replace(", (' ', 'PUNCT'), ","],[")
      
        sentens=[clean]
        
        values.append(sentens)
    
     return values

def opencsvWatTrip():
    with open('./FileCSV1/wat_trip_clean_translated.csv', encoding="utf8") as csvfile:
     Readpromthep = csv.reader(csvfile)
     values= []
     for row in Readpromthep:
        list_word = deepcut.tokenize(row[1])    
        
        senten = pos_tag(list_word, corpus='orchid_ud')

        test = str(senten)
        clean = test.replace(", (' ', 'PUNCT'), ","],[")
      
        sentens=[clean]
        
        values.append(sentens)
     return values



# save csv file
# prom
def savecsvPromGoogle():

    PromthepGoogle = opencsvPromGoogle()

    with open('./Quzi1/promthep_google.csv', mode='w',encoding="utf8",newline='') as savecsvfile:

      fieldnames = ['PromthepGoogle']
      


      writer = csv.DictWriter(savecsvfile,fieldnames=fieldnames)
      writer.writeheader()
      for row in PromthepGoogle :
          writer.writerow({'PromthepGoogle':row})
      
      print("Success save to CSV promthep google ")
def savecsvPromTrip():

    
    PromthepTrip = opencsvPromTrip()


    with open('./Quzi1/promthep_trip.csv', mode='w',encoding="utf8",newline='') as savecsvfile:

      fieldnames = ['PromthepTrip']
      writer = csv.DictWriter(savecsvfile,fieldnames=fieldnames)
      writer.writeheader()
      for row in PromthepTrip :
          writer.writerow({'PromthepTrip':row})

      print("Success save to CSV promthep trip ")

# patong
def savecsvPatongGoogle():

    PatongGoogle = opencsvPatongGoogle() 

    with open('./Quzi1/i/patong_google.csv', mode='w',encoding="utf8",newline='') as savecsvfile:
 
      fieldnames = ['PatongGoogle']
      writer = csv.DictWriter(savecsvfile,fieldnames=fieldnames)
      writer.writeheader()
      for row in PatongGoogle :
          writer.writerow({'PatongGoogle':row})
      print("Success save to CSV patong google ")

def savecsvPatongTrip():

    PatongTrip = opencsvPatongTrip()
    with open('./Quzi1/patong_trip.csv', mode='w',encoding="utf8",newline='') as savecsvfile:

      fieldnames = ['PatongTrip']
      writer = csv.DictWriter(savecsvfile,fieldnames=fieldnames)
      writer.writeheader()
      for row in PatongTrip :
          writer.writerow({'PatongTrip':row})
      print("Success save to CSV patong trip ")
# wat
def savecsvWatGoogle():

    watGoogle = opencsvWatGoogle()
   
    with open('./Quzi1/wat_google.csv', mode='w',encoding="utf8",newline='') as savecsvfile:

      fieldnames = ['watGoogle']
      writer = csv.DictWriter(savecsvfile,fieldnames=fieldnames)
      writer.writeheader()
      for row in watGoogle :
          writer.writerow({'watGoogle':row})
      print("Success save to CSV wat google ")
def savecsvWatTrip():
   
    watTrip = opencsvWatTrip()
    with open('./Quzi1/wat_trip.csv', mode='w',encoding="utf8",newline='') as savecsvfile:

      fieldnames = ['watTrip']
      writer = csv.DictWriter(savecsvfile,fieldnames=fieldnames)
      writer.writeheader()
      for row in watTrip :
          writer.writerow({'watTrip':row})         
      print("Success save to CSV wat trip ")


def main():
    # opencsvPatongGoogle()
    savecsvPatongGoogle()
    

main()