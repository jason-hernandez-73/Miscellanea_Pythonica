# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from splinter import Browser
import mission_to_mars

# @TODO: Initialize your Flask app here
app=Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/missions_to_mars")

# @TODO:  Create a route and view function that takes in a string and renders index.html template
@app.route("/")
def home():
    # this function has to retrieve data from the MongoDB
    records=mongo.db.collection.find_one()
    print(records)
    return render_template('index.html', mars=records)
    
@app.route("/scrape")
def scrape():
    # this function calls the scraper, which stores results into the MongoDB
    collection=mongo.db.collection
    # scrape from url
    data=mission_to_mars.scrape_info()
    # stores data into MongoDB
    collection.replace_one({}, data, upsert=True)
    return "Success! "
    redirect("/")
    
    

if __name__ == "__main__":
    app.run(debug=True)
