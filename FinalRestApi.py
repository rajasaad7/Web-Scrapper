import pymysql as myth

from flask import Flask, jsonify

conn = myth.connect(host="localhost" , user = "root" , password = "" , db = "maldomlist")
first = conn.cursor()
global ip
ip = "31.148.219.11"
def database(thinking):
    global date 
    global domain 
    global ipv
    global description
   
    sqlget = str("SELECT * FROM `maldomlist` WHERE ip = '"+str(ip)+"' ")
    first.execute(sqlget)
    retrived = first.fetchall()
    for row in retrived:
       date = row[0]
       domain = row[1]
       ipv = row[2]
       description = row[3]
#    print (date , domain , ipv , description)
    global jsoninfo  
    jsoninfo = [{'date' : date}, {'domain' : domain},{'ip' : ip},{'description' : description} ]
       
app = Flask(__name__)
database(1)
#These Are Good In Working !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

@app.route('/ipsearch', methods = ['GET'])
def test():
    database(1)
    return jsonify({'Message' : "Enter IP In the Adress Bar"})


@app.route('/ipsearch/<string:name>', methods = ['GET'])
def returnAll(name):
   # jsons = [sonic for sonic in jsoninfo if sonic['name'] == name]
    global ip
    ip = name
    database(1)
    return jsonify({'Information' : jsoninfo  })


if __name__ == '__main__':
    app.run(debug=True, port=8080)
