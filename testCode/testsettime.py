import schedule
import time
import datetime
from progress.bar import IncrementalBar

def job():
   datas = range(100000)
   max=len(datas)
   bar = IncrementalBar(f'Progress',max=max,
                    suffix='%(percent)d%% %(elapsed_td)s')
   for i in datas :
    for j in range(i):
        # print (i, end=' ')
     bar.next()
   bar.finish()

job()

