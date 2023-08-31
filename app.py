from flask import Flask

app = Flask("meu app")

@app.route('/')
def hello():
    return "Hello World com Flask"

@app.route('/novo')
def novo():
    return "Bye World com Flask"