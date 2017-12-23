import os
from flask import Flask
app = Flask(_name_)
@app.route("/")
def main():
return "Welcome to the world of attached bathrooms"
@app.route("/hello")
def hello():
    return "Hello Pranathi, Sahithi"
if __name__ == "__main__":
app.run(host='0.0.0.0', port=int('8001')
