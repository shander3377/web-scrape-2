from bs4 import BeautifulSoup
import requests
import time, csv
import pandas as pd 

url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page = requests.get(url)
temp_list= []
soup = BeautifulSoup(page.text, "html.parser")
table = soup.find_all('table')
tr = table[7].find_all('tr')

for t_r in tr:
    td = t_r.find_all("td")

    row = [e.text.strip() for e in td]
    temp_list.append(row)

headers = ["name", "radius", "mass", "distance"]


name = []
radius = []
mass = []
distance = []

for i in range(1,len(temp_list)):
    
    name.append(temp_list[i][0])
    radius.append(temp_list[i][8])
    mass.append(temp_list[i][7])
    distance.append(temp_list[i][5])


df = pd.DataFrame(list(zip(name,radius,mass,distance,)),columns=['Star_name','Distance','Mass','Radius'])

df.to_csv('scrap9.csv')
