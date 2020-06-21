from flask import Flask , jsonify
import csv,json
import deepcut
import pandas as pd

app = Flask(__name__)

@app.route('/sentapiProjects')
def home(): 


 csv_file = pd.DataFrame(pd.read_csv("./FileCSV1/patong_trip_clean_translated.csv", sep = ",", header = 0, index_col = False))
 csv_file.to_json("./file.json", orient = "records", date_format = "epoch", double_precision = 10, force_ascii = True, date_unit = "ms", default_handler = None)
 
 url="./file.json"
 with open(url) as f: 
  obj = json.load(f)
  
 return json.dumps(obj,indent=4,ensure_ascii=False)

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)