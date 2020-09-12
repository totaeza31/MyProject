import json
import csv
import deepcut
import pandas as pd
import numpy as np 
from pythainlp.tag import pos_tag

def readcsv(filename):

  with open(f'./testCode/csv/{filename}.csv', encoding="utf8") as csvfile:
    readers = csv.reader(csvfile)
    lambdas=[]
    next(readers, None)
    for row in readers:
     words=row[0]
     lambdas.append(words)
    
  return lambdas

def deepcuts():
 with open('./testCode/csv/datafromwithspace1.csv', encoding="utf8") as csvfile:
    readers = csv.reader(csvfile)
    data_cut=[]
    count =0 
    next(readers, None)

    for row in readers:
     words=row[0]
    #  data = deepcut.tokenize(words)
    #  data_cut.append(data)
     data_cut.append(words)
 return data_cut



def keepfile(looplamda):
  ls = readcsv('datafromwithspace1')
  total = ''
  a =[]
  for y in ls:
   filter_object = filter(lambda a: looplamda in a, ls)
   a= list(filter_object)
   total=(str(a))
  return total

def keepfileNoun(looplamda,idword):
  ls = posWord(idword)
  a =[]
  for y in ls:
   filter_object = filter(lambda a: looplamda in a, ls)
   tee = str(filter_object)
   a= list(filter_object)
  
  return a


def posWord(looplamda):
  data = keepfile(looplamda)
  if data != '[]':
    stringdata = str(data).replace("[","").replace("'","").replace(" ","").replace("]","").replace(",","")
    list_word = deepcut.tokenize(stringdata)
    posList_word = pos_tag(list_word, corpus='orchid_ud')
    text = str(posList_word).replace(" ","")\
        .replace("),(","|").replace("|"," ").replace("'","")\
        .replace(",","-").replace("(","").replace(")","")\
        .replace("]","").replace("[","")
    texts =text.split()
    return texts
  else:
    data = 'empty'
    stringdata = str(data).replace("[","").replace("'","").replace(" ","").replace("]","").replace(",","")
    list_word = deepcut.tokenize(stringdata)
    posList_word = pos_tag(list_word, corpus='orchid_ud')
    text = str(posList_word).replace(" ","")\
        .replace("),(","|").replace("|"," ").replace("'","")\
        .replace(",","-").replace("(","").replace(")","")\
        .replace("]","").replace("[","")
    texts =text.split()
    return texts

#   tagword = pos_tag(a, corpus='orchid_ud')


def unique(splits): 
    x = np.array(splits) 
    return (np.unique(x)) 

def getDuplicatesWithCount(listOfElems):
    dictOfElems = dict()
    for elem in listOfElems:
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1    
 
    dictOfElems = { key:value for key, value in dictOfElems.items() }
    return dictOfElems

def findText1(idword):
    listOfElems = keepfileNoun('NOUN',idword)
    dictOfElems = getDuplicatesWithCount(listOfElems)
    keys=[]   
    for key, value in dictOfElems.items():
      keys.append(key)
    return keys




def findcount1(idword):
    listOfElems = keepfileNoun('NOUN',idword)
    dictOfElems = getDuplicatesWithCount(listOfElems)
    counts=[]
    for key, value in dictOfElems.items():
      counts.append(value)
    return counts

# print(findcount())
# findcount()

# def savejson():
#     dict = {'words':keys,'counts':count}
#     df = pd.DataFrame(dict)
#     df.to_csv(f'./testCode/csv/testEachword.csv', index=False)
#     print("compleate csv")
# savejson()


def main():
     data = {}
     counts =0 
     lambdas = readcsv('UniquewordDeepcutWordTestset1')
    #  fileds = ['text','test']
     fileds = ['text','value']
    #   id loolmada = ดี
    
     for looplamda in lambdas: 
        #  sentens = keepfileNoun(looplamda,)
         text = findText1(looplamda)
         value = findcount1(looplamda)
         counts +=1
         data[looplamda] = []
        #  for filed in fileds:
         data[looplamda].append({
             fileds[0]: text,
             fileds[1]: value })
         
         print(counts)
     with open('./testCode/json/testfindword1.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
main()




def testZ(value):
 print(type(value))
 if value != '':
  list_word = deepcut.tokenize(value)
  posList_word = pos_tag(list_word, corpus='orchid_ud')
  return posList_word
 else : 

  value='empty'
  list_word = deepcut.tokenize(value)
  posList_word = pos_tag(list_word, corpus='orchid_ud')
  return posList_word



