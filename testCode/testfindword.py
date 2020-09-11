import json
import csv
import deepcut
import pandas as pd
import numpy as np 

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
 with open('./testCode/csv/datafromwithspace.csv', encoding="utf8") as csvfile:
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

def savecsv(names):
    splits = test()
    dict = {'words':unique(splits)}
    df = pd.DataFrame(dict)
    df.to_csv(f'./testCode/csv/{names}.csv', index=False)

def unique(splits): 
    x = np.array(splits) 
    return (np.unique(x)) 

def test():
  data = deepcuts()
  strs = str(data)
  strdata = strs.replace("[","").replace("]","").replace(",","").replace(" ","").replace("'","")
  datacut = deepcut.tokenize(strdata)
  cutwordUnqui = unique(datacut) 
  return cutwordUnqui


main()