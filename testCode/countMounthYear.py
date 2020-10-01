import json
import csv
import deepcut
import pandas as pd
import numpy as np 
from progress.bar import IncrementalBar

# นับเเถวว่ามีข้อความเท่าไรบ้างในแต่ละคอมเม้น


def readcsv(filename,mounth_year):

  with open(f'./testCode/csv/{filename}.csv', encoding="utf8") as csvfile:
    readers = csv.reader(csvfile)
    counts=0
    next(readers, None)
    for row in readers:
      # 6 is node actural with tf/idf
     words=row[5]
     if words == mounth_year:
        counts +=1
    return counts
     

def main():
    namecsv = 'dataTestset'
    years = ['2011','2012','2013','2014','2015','2016','2017','2018','2019','2020']
    mounths = ['มกราคม','กุมภาพันธ์','มีนาคม','เมษายน','พฤษภาคม','มิถุนายน','กรกฎาคม','สิงหาคม','กันยายน','ตุลาคม','พฤศจิกายน','ธันวาคม']
   
    data =[]

    for year in years:
       allcountsYear = []   
       for mounth in mounths:
           mounth_year = mounth + ' '+ year
           datas = readcsv(namecsv,mounth_year) 
           allcountsYear.append(datas)
       data.append({year:allcountsYear})
    with open(f'./testCode/json/Patong_Beach/CountsYearsMounth.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False )


main()

