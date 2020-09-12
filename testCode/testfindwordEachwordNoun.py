import json
import csv
import deepcut
import pandas as pd
import numpy as np 
from collections import Counter

def readcsv(filename):

  with open(f'./testCode/csv/{filename}.csv', encoding="utf8") as csvfile:
    readers = csv.reader(csvfile)
    lambdas=[]
    next(readers, None)
    for row in readers:
     words=row[0]
     lambdas.append(words)
    
  return lambdas

def keepfile(looplamda):
  
  ls = readcsv('datafromwithspace')
  total = ''
  for y in ls:
   filter_object = filter(lambda a: looplamda in a, ls)
   a= list(filter_object)
   total=(str(a))
  return total


def main():
     data = {}
     counts =0 
     lambdas = readcsv('UniquewordDeepcutWordTestset1')
     fileds = 'texts'
     for looplamda in lambdas: 

         sentens = keepfile(looplamda)
         counts +=1
         data[looplamda] = []
         data[looplamda].append({
             fileds: sentens })
         print(counts)

     with open('./testCode/json/UniquewordDeepcutWordTestset111.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)


def count_item(input_list):
  """count item in a list, return a dict"""
  result = {}
  for item in input_list:
    if item in result:
      # result[item] += 1
      item+=1
    else:
      # result[item] = 1
      item =1
  print(item)
  return result

animals = ['dog', 'cat', 'cat', 'dog', 'dog', 'dog', 'cat', 'dog', 'hippo']
genders = ['M', 'F', 'F', 'F', 'M']
balls = ['red', 'red', 'blue', 'blue', 'blue', 'black']


# test function
# print(count_item(animals))

# test = "('ที่', 'DET'), ('ไม่', 'PART'), ('หยุดยั้ง', 'VERB'), ('บริเวณ', 'NOUN'), ('หาด', 'NOUN')"

# aa = test.replace(" ","").replace("),(","|").replace("|"," ").replace("'","").replace(",","-").replace("(","").replace(")","")


# function to get unique values 


def readcsv():
    with open(f'./testCode/csv/testset_deepcutpythai.csv', encoding="utf8") as csvfile:
     readers = csv.reader(csvfile)
     data = []
     count=0
     next(readers, None)

     for row in readers:
        words=row[4]
        aa = words.replace(" ","")\
        .replace("),(","|").replace("|"," ").replace("'","")\
        .replace(",","-").replace("(","").replace(")","")\
        .replace("]","").replace("[","")
        text =aa.split()
        count+=1
        data.append(text)
    return data

def main1():
    data=[]
    newdata=[]
    information = readcsv()
    strinformation = str(information)
    replacestrinformation = strinformation.replace("'",'')\
                                          .replace('[','')\
                                          .replace(']','')\
                                          .replace(' ','')\
                                          .replace('\"','')\
                                          .replace('.','')\
                                          .replace(',',' ')                            
    splits= replacestrinformation.split()

    
    # print(splits)
    # cutwordUnqui = unique(splits) 
    return splits


def keepfile(looplamda):
  
  ls = main1()
  total = ''
  a = []
  count=0
  for y in ls:
   filter_object = filter(lambda a: looplamda in a, ls)
   a= list(filter_object)
   count+=1
   print("count of finding NOUN >>",count)
  #  total=(str(a))

  # replaceNoun = total.replace("-NOUN","")
  # print(type(a))
  # print(a)
  return a


def main():
     data = {}
     counts =0 
     lambdas = ['NOUN']
     fileds = 'texts'
     for looplamda in lambdas: 

         sentens = keepfile(looplamda)

         counts +=1
         data[looplamda] = []
         data[looplamda].append({
             fileds: sentens })
     return data


     
     
     with open('./testCode/json/testEachword.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)



# datas = keepfile('NOUN')
# listOfElems = "['Hello', 'Ok', 'is', 'Ok', 'test', 'this', 'is', 'a', 'test']"
# print(type(datas))
# countItem= count_item(listOfElems)

# aa = ''
# straa = str(countItem).replace("-NOUN","").replace("{","[").replace("}","]")

# print(straa)
# print(countItem)


# savejson()


def getDuplicatesWithCount(listOfElems):
    dictOfElems = dict()
    for elem in listOfElems:
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1    
 
    dictOfElems = { key:value for key, value in dictOfElems.items() }
    return dictOfElems


listOfElems = keepfile('NOUN')
# Get a dictionary containing duplicate elements in list and their frequency count
dictOfElems = getDuplicatesWithCount(listOfElems)
keys=[]     
count=[]
for key, value in dictOfElems.items():
  keys.append(key)
  count.append(value)


def savejson():
    dict = {'words':keys,'counts':count}
    df = pd.DataFrame(dict)
    df.to_csv(f'./testCode/csv/testEachword.csv', index=False)
    print("compleate csv")
savejson()