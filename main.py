from flask import Flask, render_template, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(os.environ.get("LOCAL_HOST"))
db = client["mydb"]
collection = db["user"]


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')

        # Insert data into MongoDB
        data = {"name": name, "email": email}
        collection.insert_one(data)

    return render_template("index.html", )

if __name__ == "__main__":
    app.run(debug=True)