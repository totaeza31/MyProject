 

def keepfile(looplamda):
  ls = ['Hello from AskPython', 'แออัดมาก', 'Hello boy!', 'ไม่ค่อยแออัดมาก']
  total = ''
  for y in ls:
   filter_object = filter(lambda a: looplamda in a, ls)
   a= list(filter_object)
   total=(str(a))
  return total


def datass():
    keepfilea = keepfile()
    print(keepfilea) 

def main():
     counts =0 
     lambdas = ['แออัด','Hello']
     for looplamda in lambdas: 
         aa=keepfile(looplamda)
         counts +=1
         print("count",counts,"text",looplamda,"senten",aa)

main()