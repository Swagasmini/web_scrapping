import pandas as pd
import requests 
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=35.0077&lon=-81.0218#.Xsrri0Qza1s")
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(id='seven-day-forecast')
#print(week)
items = week.find_all(class_= 'tombstone-container')
#print(items[0])

#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
##print(items[0].find(class_='temp').get_text())

##List_comprehensions

periods_names = [item.find(class_='period-name').get_text() for item in items]

#print(periods_names)
short_desc = [item.find(class_='short-desc').get_text() for item in items]
#print(short_desc)
temp = [item.find(class_='temp').get_text() for item in items]
#print(temp)


##Using Pandas


weather_stuff = pd.DataFrame (
  {
  'period':periods_names,
  'Short_desc': short_desc,
  'temperature': temp,
  })
  
print(weather_stuff)
weather_stuff.to_csv('weather.csv')