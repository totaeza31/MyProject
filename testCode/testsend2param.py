import json
import csv
import deepcut
import pandas as pd
import numpy as np 
from progress.bar import IncrementalBar


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


def readscountAll():
    data = readcsv('test_p95_t71')
    allList = []
    # datacheckword = ['posPosNeg']
    namePosNeg =['pos','neg']
    nameSenten =['ADJ','NOUN','VERB','ADV']
    for num_namePosNeg in namePosNeg:
     checkword = CheckWordPosNeg(num_namePosNeg,data)
     replacea = checkword.replace("'",'').replace("[",'').replace("]",'').replace("pos",'').replace(" ",'').replace("neg",'')
     splits= replacea.split(',')
     for num_nameSenten in nameSenten:
      checkSenten = CheckSentens(splits,num_nameSenten)
      allList.extend(checkSenten)
    return allList

def readscount(namePosNeg,readsenten):
    data = readcsv('test_p95_t71')
    # datacheckword = ['posPosNeg']
    checkword = CheckWordPosNeg(namePosNeg,data)
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

def findText(namePosNeg,readsenten):
    listOfElems = readscount(namePosNeg,readsenten)

    dictOfElems = getDuplicatesWithCount(listOfElems)
    dataJson = []
    for key, value in dictOfElems.items():
        dataJson.append({"word":key,"count":value})
    return dataJson

def findTextShowall(namePosNeg,readsenten):
    listOfElems = readscountAll()
    dictOfElems = getDuplicatesWithCount(listOfElems)
    dataJson = []
    for key, value in dictOfElems.items():
        dataJson.append({"word":key,"count":value})
    return dataJson

# print(findText1())

def main():
    data = {}
    counts =0 
    namePositiveNegative=['pos','neg']
    namesentenCloud = ['NOUN','VERB','ADV','ADJ']
    for namePosNeg in namePositiveNegative:
     for readsenten in namesentenCloud:
      namepath = namePosNeg+readsenten
      lambdas = findText(namePosNeg,readsenten)

      data[namepath] = lambdas
      print("Processing complete in >> ",namepath)

    data['all']= findTextShowall()

    with open(f'./testCode/json/WordClould.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False )
# main()


# main()