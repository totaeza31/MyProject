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
    next(readers, None)
    for row in readers:
     words=row[0]
     replaceWord = words.replace("-NOUN","").replace("-VERB","").replace("-ADJ","").replace("-ADV","")
     lambdas.append(replaceWord)
    
  return lambdas

# def deepcuts():
#  with open('./testCode/csv/datafromwithspace.csv', encoding="utf8") as csvfile:
#     readers = csv.reader(csvfile)
#     data_cut=[]
#     count =0 
#     next(readers, None)

#     for row in readers:
#      words=row[0]
#     #  data = deepcut.tokenize(words)
#     #  data_cut.append(data)
#      data_cut.append(words)
#  return data_cut



def keepfile(looplamda):
  
  ls = readcsv('datafromwithspace')
  # total = []
  for y in ls:
   filter_object = filter(lambda a: looplamda in a, ls)
   a= list(filter_object)
  #  total=(str(a))\
  return a


def main():
    data = {}
    counts =0 
    namecsv = ['NOUN','VERB','ADV','ADJ']
    name='testEachword'
    for readname in namecsv:
     lambdas = readcsv(name+readname)
     max = len(lambdas)
     bar = IncrementalBar(f'Word segment file {readname}',max = max ,
           suffix='%(percent)d%% %(elapsed_td)s')
    #  fileds = 'texts'
     data[readname] = []
     for looplamda in lambdas: 
      sentens = keepfile(looplamda)
      bar.next()
      if sentens != []:
      
        #  for filed in fileds:
       data[readname].append({
             looplamda: sentens,
             })
      # ranges_sentens = len(sentens)
      #  data.append({looplamda:sentens})
       counts+=1
      else:
       counts=counts
     bar.finish()
    #  print(counts)
      # สร้าง json แบบ {{name:}{name:}} ใช้ ranges
      # for ranges in range(ranges_sentens):
      # data[looplamda].append({
          # looplamda: sentens[ranges] })
          # looplamda: sentens })
    
    with open(f'./testCode/json/UniquewordDeepcutWordADJADVNOUNVERB.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False )


def unique(splits): 
    x = np.array(splits) 
    return (np.unique(x)) 


main()