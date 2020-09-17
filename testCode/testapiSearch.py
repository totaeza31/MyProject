from flask_restful import Api, Resource ,output_json
from flask import Flask , jsonify
from flask.ext.restful import reqparse, abort
import json

app = Flask(__name__)
api = Api(app)

class Helloword(Resource):
    def get(self,name):
        url = './testCode/json/UniquewordDeepcutWordTestsetNomal.json'     
        with open(url,encoding="utf-8") as f: 
          names = json.load(f)
          # obj = names[name]
        return  make_response(names[name])
        # return names[name]
api.add_resource(Helloword,"/helloword/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)