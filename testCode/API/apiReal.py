from flask import Flask , jsonify
from flask_restful import testCode, Resource,reqparse, abort
import csv,json
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
testCode = testCode(app)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response
  

#  จำนวน comment in mounth / year 
@app.route('/year')
def CountYears(): 
 
 url="./testCode/json/CountsYearsMounth.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)


@app.route('/allcomments')
def allcomment(): 
 
 url="./testCode/json/dataTestset.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,indent=4,ensure_ascii=False)
 
class ClickEachwordAndText(Resource):
    def get(self,name):
        url = './testCode/json/UniquewordDeepcutWordADJADVNOUNVERBNtesttest.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]
  
class WordCloud(Resource):
    def get(self,name):
        url = './testCode/json/WordClould.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]

class Piechart(Resource):
    def get(self,name):
        url = './testCode/json/CountsPieChart.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]

class ADJADVNOUN(Resource):
    def get(self,name):
        url = './testCode/json/UniquewordDeepcutWordADJADVNOUNVERB.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]

#  จำนวน topten 
# /posNOUN /posVERB /posADJ /posADV /negNOUN /negVERB /negADJ /negADV

class topten(Resource):
    def get(self,name):
        url = './testCode/json/toptensentens.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]

# จำนวน คำทั้งหมด positive,negative ทั้งหมด 
# /pos /neg /all
class Counts(Resource):
    def get(self,name):
        url = './testCode/json/Counts.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
     
        return  names[name]


# posgard >> /postgards/POSNOUN /POSVERB /POSADJ /POSADV /NEGNOUN /NEGVERB /NEGADJ /NEGADV
class Postgard(Resource):
    def get(self,name):
        url = './testCode/json/Postgards.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
        return  names[name]


testCode.add_resource(Postgard,"/postgrards/<string:name>")
testCode.add_resource(Counts,"/counts/<string:name>")
testCode.add_resource(topten,"/topten/<string:name>")
testCode.add_resource(Piechart,"/piechart/<string:name>")
testCode.add_resource(ADJADVNOUN,"/senten/text/test/<string:name>")
testCode.add_resource(ClickEachwordAndText,"/senten/text/<string:name>")
testCode.add_resource(WordCloud,"/wordcloud/<string:name>")

if __name__ == '__main__':
   app.run(host="localhost", port=5000, debug=True)
    #  app.run(host="testCode.playz-th.com", port=5000, debug=True)
