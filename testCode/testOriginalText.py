import csv
import pandas as pd
import json
def readcsv(filename):
  data = []
  name=['Id','Review']
  with open(f'./testCode/csv/{filename}.csv', encoding="utf8") as csvfile:
    readers = csv.reader(csvfile)
    next(readers, None)
    for row in readers:
     Ids=row[0]
     Review=row[1]
     Thai=row[2]
     Rating=row[4]
     Time=row[5]
     data.append({name[0]:Ids,name[1]:Review,"Thai":Thai,"Rating":Rating,"Time":Time})
    
  return data

def main():

    data = readcsv('dataTestset')
    with open('./testCode/json/dataTestset.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
main()