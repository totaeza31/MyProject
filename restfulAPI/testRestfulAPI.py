from flask import Flask , jsonify
import csv,json
import deepcut

app = Flask(__name__)

@app.route('/sentapiProjects')
def home(): 
 csvFilePath = './FileCSV1/patong_trip_clean_translated.csv'
 data={}
 with open(csvFilePath, encoding="utf8") as csvFile:
    csvReader = csv.DictReader(csvFile)
    for row in csvReader:
        list_word = row['th']
        data[list_word] = row

 return json.dumps(data,indent=4,ensure_ascii=False)




if __name__ == '__main__':
   app.run(host="0.0.0.0", port=5000, debug=True)