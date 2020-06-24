from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route('/')
def home():
     # Find one record of data from the mongo database
    mars_data = mongo.db.collection.find_one()
    # Return template and data
    return render_template("index.html", mars=mars_data)

@app.route('/scrape')
def scrape():

     # Run the scrape function
    mars_scraped = mars_scrape.scrapeinfo()

    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_scraped, upsert=True)

    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
