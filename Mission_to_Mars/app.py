from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

client = pymongo.MongoClient('mongodb://localhost:27017')

db = client.mars_db

Mars_data = scrape_mars.scrape()
db.scrape.update({}, Mars_data, upsert=True)

@app.route("/")
def queryDB():

    listings = db.scrape.find_one()
    return render_template("index.html", listings=listings)

@app.route("/scrape")
def BuildDB():

    Mars_data = scrape_mars.scrape()
    db.scrape.update({}, Mars_data, upsert=True)
    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(debug=True)