# import necessary libraries
from flask import Flask, render_template
from flask_pymongo import PyMongo
import # other code file

# @TODO: Initialize your Flask app here
app=Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mission_to_mars")

# @TODO:  Create a route and view function that takes in a string and renders index.html template
@app.route("/")
def home():

    # Find one record of data from the mongo database
    # variable = mongo.db. # collection .find_one()

    # Return template and data
    return render_template("index.html", # variable = from above)

@app.route("/scrape")
def scrape():
    news_title =
    news_p =
    return render_template("index.html")

    redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
