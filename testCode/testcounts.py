import json
import csv
import deepcut
import pandas as pd
import numpy as np 
from progress.bar import IncrementalBar

# นับเเถวว่ามีข้อความเท่าไรบ้างในแต่ละคอมเม้น


def readcsv(filename,posneg):

  with open(f'./testCode/csv/{filename}.csv', encoding="utf8") as csvfile:
    readers = csv.reader(csvfile)
    counts=0
    next(readers, None)
    for row in readers:
      # 6 is node actural with tf/idf
     words=row[6]
     if words == posneg:
        counts +=1
    return counts
     

def main():
    namecsv = 'test_p95_t7'
    posnegs = ['pos','neg']
    allcounts = 0   
    data ={}
    for posneg in posnegs:
     datas = readcsv(namecsv,posneg)  
    
     data[posneg]=[]
     data[posneg].append({'numComment':datas})
    
     allcounts += datas
    data['all']=[]
    data['all'].append({'numComment':allcounts})
    with open(f'./testCode/json/Patong_Beach/Counts.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False )


main()

