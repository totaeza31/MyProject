import pandas as pd
import mysql.connector

def connect2():
 hosting = "172.26.117.6"
 username = "aitasireadonly" 
 password = "aitasipassword"
 database_name = "dataretrival"


 mydb = mysql.connector.connect(
    host = hosting,
    user = username,
    passwd = password,
    database = database_name
 )


 mycursor2 = mydb.cursor()
 mycursor2.execute("SELECT DISTINCT RD_ID,RD_MESSAGE,RD_SCORE,RD_VISIT_DATE FROM vw_attraction_score \
                   WHERE AT_OTA_NAME='tripadvisor' \
                   and AI_NAME= 'Patong Beach'   \
                   and (RD_MESSAGE like '%a%' or RD_MESSAGE like'%e%'or RD_MESSAGE like'%i%'or RD_MESSAGE like'%o%'or RD_MESSAGE like'%u%')   \
                   and  RD_MESSAGE NOT like'%http%'   \
                   and  RD_MESSAGE NOT like'%Read more%'   \
                   and  RD_VISIT_DATE !=''   \
                   and (RD_SCORE = '1'or RD_SCORE = '2') \
                   ORDER BY RAND() LIMIT 20\
                   " )
 myresult2 = mycursor2.fetchall()


 data=[]
 datascore=[]
 rd_id=[]
 date = []
 for x in myresult2:
   message=x[1]
   data.append(message)
   score=x[2]
   datascore.append(score)
   rdid=x[0]
   rd_id.append(rdid)
   dates=x[3]
   date.append(dates)

 return {'RD_ID':rd_id,'RD_MESSAGE':data,'RD_SCORE':datascore,'RD_VISIT_DATE':date}


def SaveCSVall2():

    dict = connect2()
    df = pd.DataFrame(dict)
    df.to_csv(f'./testdatabaseAJ.csv', index=False)


SaveCSVall2()