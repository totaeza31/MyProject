from flask_restful import Api, Resource ,output_json
from flask import Flask , jsonify
import json

app = Flask(__name__)
api = Api(app)

class Helloword(Resource):
    def get(self,name,):
        url = './testCode/json/UniquewordDeepcutWordADJADVNOUNVERB.json'     
        with open(url,encoding='utf-8') as f: 
          names = json.load(f)
          # obj = names[name]
        # return 
        return names[name]
api.add_resource(Helloword,"/helloword/<string:name>")

@app.route('/CorrectIDFRatingType1Patong')
def CorrectIDFRatingType1Patong(): 
 
 url="./testCode/json/UniquewordDeepcutWordTestsetNomalReal1.json"
 with open(url, encoding="utf8") as f: 
  obj = json.load(f)
 return json.dumps(obj,ensure_ascii=False)


if __name__ == "__main__":
    app.run(debug=True)