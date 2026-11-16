from flask import Flask, request


app = Flask(__name__)

@app.route('/')
def index():
    return {"message": "Welcome to the API!"}