import json
import csv
import deepcut
import pandas as pd
import numpy as np 
from progress.bar import IncrementalBar

from operator import itemgetter 
def readcsv(filename):

  with open(f'./testCode/csv/{filename}.csv', encoding="utf8") as csvfile:
    readers = csv.reader(csvfile)
    lambdas=[]
    worda = []
    next(readers, None)
    for row in readers:
     words=row[0]
     posneg=row[6]
     replaceWord = words.replace("[","").replace("]","").replace(" ","").replace("'","")
     lambdas.append(replaceWord+posneg)
   
  return lambdas

def CheckWordPosNeg(looplamda,data):
  total=''
#   ls = readcsv('datafromwithspace')
  for y in data:
   filter_object = filter(lambda a: looplamda in a, data)
   a= list(filter_object)
   total=(str(a))
  return total

def CheckSentens(splits,looplamda):

#   ls = readcsv('datafromwithspace')
  for y in splits:
   filter_object = filter(lambda a: looplamda in a, splits)
   a= list(filter_object)
#    total=(str(a))
  return a


def readscountAll(datacsv):
    allList = []
    # datacheckword = ['posPosNeg']
    namePosNeg =['pos','neg']
    nameSenten =['ADJ','NOUN','VERB','ADV']
    for num_namePosNeg in namePosNeg:
     checkword = CheckWordPosNeg(num_namePosNeg,datacsv)
     replacea = checkword.replace("'",'').replace("[",'').replace("]",'').replace("pos",'').replace(" ",'').replace("neg",'')
     splits= replacea.split(',')
     for num_nameSenten in nameSenten:
      checkSenten = CheckSentens(splits,num_nameSenten)
      allList.extend(checkSenten)
    return allList

def readscount(namePosNeg,readsenten,datacsv):
   
    # datacheckword = ['posPosNeg']
    checkword = CheckWordPosNeg(namePosNeg,datacsv)
    replacea = checkword.replace("'",'').replace("[",'').replace("]",'').replace("pos",'').replace(" ",'').replace("neg",'')
    splits= replacea.split(',')
    checkSenten = CheckSentens(splits,readsenten)
    return checkSenten


def getDuplicatesWithCount(listOfElems):
    dictOfElems = dict()
    for elem in listOfElems:
        if elem in dictOfElems:
            dictOfElems[elem] += 1
        else:
            dictOfElems[elem] = 1    
 
    dictOfElems = { key:value for key, value in dictOfElems.items() }
    return dictOfElems

def findText(namePosNeg,readsenten,datacsv):
    listOfElems = readscount(namePosNeg,readsenten,datacsv)

    dictOfElems = getDuplicatesWithCount(listOfElems)
   
    d={}
    # dataJson.append("Words","Count")
    for key, value in dictOfElems.items():
        datastr = str(key)
        replacestr = datastr.replace("-NOUN","").replace("-VERB","")\
                            .replace("-ADJ","").replace("-ADV","")\
                            .replace("(","").replace(")","")

        d[replacestr] = value
    return d

def readDataFarm(namePosNeg,readsenten,datacsv):
    data = findText(namePosNeg,readsenten,datacsv)
    dicts ={}
    res = dict(sorted(data.items(), key = itemgetter(1), reverse = True)[:10]) 
    dictlist=[] 
    filds = ["Words","Counts"]
    dictlist.append(filds) 
    for key, value in res.items(): 
        temp = [key,value] 
        dictlist.append(temp) 
    return dictlist

def readDataFarmall(datacsv):
    data = findTextShowall(datacsv)
    dicts ={}
    res = dict(sorted(data.items(), key = itemgetter(1), reverse = True)[:10]) 
    dictlist=[] 
    filds = ["Words","Counts"]
    dictlist.append(filds) 
    for key, value in res.items(): 
        temp = [key,value] 
        dictlist.append(temp) 
    return dictlist  
   
def findTextShowall(datacsv):
    counts=0
    d={}
    listOfElems = readscountAll(datacsv)
    dictOfElems = getDuplicatesWithCount(listOfElems)
    for key, value in dictOfElems.items():
        datastr = str(key)
        replacestr = datastr.replace("-NOUN","").replace("-VERB","")\
                            .replace("-ADJ","").replace("-ADV","")\
                            .replace("(","").replace(")","")

        d[replacestr] = value
    return d

# print(findText1())

def main():
    data = {}

    namePositiveNegative=['pos','neg']
    namesentenCloud = ['NOUN','VERB','ADV','ADJ']
    datacsv = readcsv('test_p95_t7')
    for namePosNeg in namePositiveNegative:
    #  sentens =[]
     for readsenten in namesentenCloud:
      
      lambdas = readDataFarm(namePosNeg,readsenten,datacsv)
      lambdasSenten = namePosNeg+readsenten

    #   sentens.append(lambdas)
      data[lambdasSenten] = lambdas
    
      print("Processing complete in >> ",lambdasSenten)
    
    lamda = readDataFarmall(datacsv)
    data['all']= lamda
    print("compleate")
    with open(f'./testCode/json/toptensentens.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False )
main()


# main()