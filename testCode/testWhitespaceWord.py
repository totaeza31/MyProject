import numpy as np 
import csv
import pandas as pd
# function to get unique values 
def unique(splits): 
    x = np.array(splits) 
    print(np.unique(x)) 
    return (np.unique(x)) 
      

def readcsv():
    with open(f'./testCode/csv/data.csv', encoding="utf8") as csvfile:
     readers = csv.reader(csvfile)
     data = []
     count=0
     next(readers, None)

     for row in readers:
        words=row[2]
        text =words.split()
        count+=1
        data.append(text)
    return data

def main():
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
    print(type(splits))
    print(splits)
    cutwordUnqui = unique(splits) 
    return cutwordUnqui

def savejson():
    dict = {'words':main()}
    df = pd.DataFrame(dict)
    df.to_csv(f'./testCode/csv/testUniqui.csv', index=False)

savejson()

