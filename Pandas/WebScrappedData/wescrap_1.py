#%%

import pandas as pd

import requests
from bs4 import BeautifulSoup

url = "https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page=1"


headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

webpage  = requests.get(url, headers=headers).text


soup = BeautifulSoup(webpage,'lxml')


# p = soup.find_all('div', class_="companyCardWrapper__companyRating")

# print(p)

# rating = soup.find_all("div", class_="rating_text")

# ratings = []
# for i in rating:
#     ratings.append(i.text.strip())
    

company = soup.find_all('div',class_="companyCardWrapper")

print(len(company))


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

print(df)
    



# %%
