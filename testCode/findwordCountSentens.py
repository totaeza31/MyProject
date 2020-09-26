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
 
    counts=0
    for key, value in dictOfElems.items():
        datastr = str(key)
        replacestr = datastr.replace("-NOUN","").replace("-VERB","")\
                            .replace("-ADJ","").replace("-ADV","")\
                            .replace("(","").replace(")","")
        # dataJson.append({"word":replacestr,"count":value})
        counts += value
    return counts

def findTextShowall(datacsv):
    counts=0

    listOfElems = readscountAll(datacsv)
    dictOfElems = getDuplicatesWithCount(listOfElems)
    for key, value in dictOfElems.items():
        datastr = str(key)
        replacestr = datastr.replace("-NOUN","").replace("-VERB","")\
                            .replace("-ADJ","").replace("-ADV","")\
                            .replace("(","").replace(")","")

        counts += value
    return counts

# print(findText1())

def main():
    data = {}
    counts =0 
    
    namePositiveNegative=['pos','neg']
    namesentenCloud = ['NOUN','VERB','ADV','ADJ']
    datacsv = readcsv('test_p95_t7')
    for namePosNeg in namePositiveNegative:
     sentens =[]
     for readsenten in namesentenCloud:
      
      lambdas = findText(namePosNeg,readsenten,datacsv)
      lambdasSenten = (readsenten,lambdas)
      sentens.append(lambdasSenten)
     data[namePosNeg] = sentens

     print("Processing complete in >> ",namePosNeg)
    lamda = findTextShowall(datacsv)
    data['all']= lamda
    print("compleate")
    with open(f'./testCode/json/CountsPieChart.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False )
main()


# main()