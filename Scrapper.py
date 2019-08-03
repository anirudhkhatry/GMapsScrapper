import requests
import requests, json ,csv
  
api_key = ''
  
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
  
q = input('Search query: ') 
query=q.replace(' ','+')  
r = requests.get(url + 'query=' + query +
                        '&key=' + api_key) 
  
x = r.json()
y = x['results']

for i in range(len(y)):  
    print(y[i]['name']+'\t') 

f = open('C:/Users/Anirudh/Desktop/GData.csv','w',encoding='utf-8',newline='')
csv_writer=csv.writer(f)
c=0
for res in y:
    #if(c==0):
    #    csv_writer.writerow(res.keys())
    #csv_writer.writerow(res.values())
    #c=c+1
    try:
        place_id=str(res['id'])
        url2="https://maps.googleapis.com/maps/api/place/details/json?placeid="+place_id+"&key="+api_key
    
    except KeyError:
        pass
    r2=requests.get(url2)
    x2=r2.json()
    
    print(x2)    

f.close()
