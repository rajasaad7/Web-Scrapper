import requests
from bs4 import BeautifulSoup
import pymysql as myth

conn = myth.connect(host="localhost" , user = "root" , password = "" , db = "maldomlist")
first = conn.cursor()
casual = "update me"


data = [] 
abc = None
mark = None
counter = 4
counter2 = 0
sr = 0
def spider(page):
    #ip = input("Enter Ip or Domain Name etc : ")
    
    # if want to search use url1 instead of url
    
    #  url1 = 'http://www.malwaredomainlist.com/mdl.php?search='+str(ip)+'&colsearch=All&quantity=50'
    
    url = 'http://www.malwaredomainlist.com/mdl2.php?search=&colsearch=All&quantity=100&page='+str(page)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html5lib")
    find_text = soup.find( "div", {"class":"ContentBox"}  )
    
    rows=list()
    global data
    rows = find_text.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele ])
    doings()
def doings():
    try:
        global counter
        global sr
        abc = '?'.join(data[counter])
        counter = counter + 1 
        
        sr = sr + 1
        global mark
        mark = abc.split('?')
        #print("{\n 'date' : '"+mark[0]+"',")
        #print(" 'domain' : '"+mark[1]+"',")
        #print(" 'IP' : '"+mark[2]+"',")
        #print(" 'description' : '"+mark[4]+"'\n}")
        database()

    except:
        print ("Page "+counter2+" Ends Here !!")
  

def database():
    
    first.execute("INSERT INTO `maldomlist`(`Sr Number`, `date`, `domain`, `ip`, `discription`) VALUES (%s,%s,%s,%s,%s) """ , (sr , mark[0] , mark[1],mark[2],mark[4]))
    try:
        # Commit your changes in the database
        conn.commit()
        print('Changes Successfull !!')
        loop()
        
    except:
        # Rollback in case there is any error
        conn.rollback()
        print("Page "+str(counter2)+" Ends Here !!")
        
        
def loop():
    if(mark[0] != None ):
        print(counter)
        doings()#                     It Is Writing First 5 pages from maldomlist to my local hosted database !! you can scrapp whole database by changing..
     

while (counter2<=5):  #by changing this 5 to 25 all the data is scrapped...
    spider(counter2)
    counter = 4
    counter2 = counter2 + 1


print('Program Has Been Ended !!')
    