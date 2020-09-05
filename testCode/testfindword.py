import json

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
     data = {}
     counts =0 
     lambdas = ['boy','Hello']
     fileds = 'texts'
     for looplamda in lambdas: 

         sentens = keepfile(looplamda)
         counts +=1
         print("count",counts,"text",looplamda,"senten",sentens)
         data[looplamda] = []
         data[looplamda].append({
             fileds: sentens })
     with open('./testCode/json/datatesid.json', 'w') as outfile:
        json.dump(data, outfile)
main()
