from flask import Flask, render_template
import scrape
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.scrape_db

# Drops collection if available to remove duplicates
db.scrape.drop()

# Creates a collection in the database and inserts two documents  


def index():
    mars_dict = client.db.mars_collection.find_one()
    return render_template("index.html", mars=mars_dict)


@app.route("/scrape")
def scraper():
    mars_collection = client.db.mars_collection
    mars_data = scrape.scrape()
    mars_collection.update({}, mars_data, upsert=True)


if __name__ == "__main__":
    app.run(debug=True)