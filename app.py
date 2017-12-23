import os
from flask import Flask
app = Flask(_name_)
@app.route("/")
def main():
return "Welcomr to the world of attached bathrooms"

if __name__ == "__main__":
app.run(host='0.0.0.0', port=int('8001')
