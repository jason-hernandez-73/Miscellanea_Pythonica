# Dependencies
import pandas as pd
import requests
from pprint import pprint
import pymongo
from bs4 import BeautifulSoup as bs
from splinter import Browser
import lxml

# Nasa's Mars News Site
url = "https://mars.nasa.gov/news/"

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

# Set up MongoDB
conn='mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define database
db = client.missions_to_mars
collection = db.mars_news

# Retrieve page with the requests module
# response = requests.get(url)
# html = response.text
browser.visit(url)  
html = browser.html
# Create BeautifulSoup object; parse with 'html.parser'
soup = bs(html, 'html.parser')

# THIS BLOCK NEEDS TO BE FIXED
# Assign variables
# slide = soup.find('li', class_='image_and_description_container')
# print(slide)
#news_title = soup.find('div', class_='content_title')
# news_title_text = news_title.a.text
# news_p = soup.find('div', class_='article_teaser_body')
#print(news_title)
# print(news_p)

# Add to MongoDB
post = {
    'title': news_title,
    'paragraph': news_p
}

collection.insert(post)

# Splinter to featured image
featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(featured_image_url)

# Twitter - code from Vicky and Tracy, after a lot of troubleshootong!
all_tweets = []
twitter_url = 'https://twitter.com/marswxreport?lang=en'
data = requests.get(twitter_url)
html = bs(data.text, 'html.parser')
timeline = html.select('#timeline li.stream-item')
for tweet in timeline:
    tweet_id = tweet['data-item-id']
    tweet_text = tweet.select('p.tweet-text')[0].get_text()
    all_tweets.append({"id": tweet_id, "text": tweet_text})
    print(all_tweets)
    break
    
# Add to MongoDB
post = {
    'tweet': tweet_text
}

tweets.insert_one(post)

# Mars Facts table
facts_url = 'https://space-facts.com/mars/'
mars_table = pd.read_html(facts_url)
mars_table

#Hemisphere images
hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere",\
     "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/valles_marineris_enhanced"},
    {"title": "Cerberus Hemisphere",\
     "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"},
    {"title": "Schiaparelli Hemisphere",\
     "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/schiaparelli_enhanced"},
    {"title": "Syrtis Major Hemisphere",\
     "img_url": "https://astrogeology.usgs.gov/search/map/Mars/Viking/syrtis_major_enhanced"},
]

browser.quit()