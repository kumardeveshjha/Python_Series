#%%
import pandas as pd
import requests

import requests
from bs4 import BeautifulSoup

# this is for api call 
# url = "https://streaming-availability.p.rapidapi.com/shows/%7Btype%7D/%7Bid%7D"

# headers = {
# 	"x-rapidapi-key": "d534ff0b5fmshc5a8d25ec9be4eep1b33e1jsn325fc0bd12a1",
# 	"x-rapidapi-host": "streaming-availability.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())


# this is for web scrapr call 
for j in range(1,11):
	url = f"https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={j}"


	headers = {
				"User-Agent": (
					"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
					"AppleWebKit/537.36 (KHTML, like Gecko) "
					"Chrome/120.0.0.0 Safari/537.36"
				)
				}

	webpage  = requests.get(url, headers=headers).text

	soup = BeautifulSoup(webpage,'lxml')
	company = soup.find_all('div',class_="companyCardWrapper")

	name = []
	rating = []
	reviews = []
	culture = []

	for i in company:
		name.append(i.find('h2').text.strip())
		rating.append(i.find("div", class_="rating_text").text.strip())
		reviews.append(i.find('span', class_="companyCardWrapper__companyRatingCount").text.strip())
		culture.append(i.find('span', class_="companyCardWrapper__ratingValues").text.strip())

	data = {"name":name,"rating":rating,"reviews":reviews,"culture":culture}

	df = pd.DataFrame(data)

# print(df)
df     


# %%
