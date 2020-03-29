# import necessary libraries
from flask import Flask, render_template
from splinter import Browser
import mission_to_mars.py

# @TODO: Initialize your Flask app here
app=Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/missions_to_mars")

# @TODO:  Create a route and view function that takes in a string and renders index.html template
@app.route("/")
def home():
    return

@app.route("/scrape")
def scrape():
    data = mission_to_mars.scrape_info()

    return render_template("index.html", news_title, news_p)
    return featured_image
    return tweet_text

    redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
