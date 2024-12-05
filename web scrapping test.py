import requests
from bs4 import BeautifulSoup
import csv
a=requests.get("https://webscraper.io/test-sites/e-commerce/static")
print(a)
b=BeautifulSoup(a.content,'html.parser')
# print(b)
c=b.find_all("a",class_="title")
print(c)
for i in c:
    print(i.text)
z=open("Data3.csv","a")
q=csv.writer(z)
t=[]
for i in c:
    r=[]
    r.append(i.text)
    q.writerow(r)
    t.append(r)
print(r)



