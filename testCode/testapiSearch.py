from flask_restful import Api, Resource
from flask import Flask , jsonify
import sys
import settings
import json

app = Flask(__name__)
api = Api(app)

class Helloword(Resource):
    def get(self,name):
        url = './testCode/json/UniquewordDeepcutWordTestsetNomal.json'
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
          # obj = names[name]
        return  names[name]
        # return names[name]
api.add_resource(Helloword,"/helloword/<string:name>")


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf-8')
    app.run(debug=True)