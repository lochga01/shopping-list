<<<<<<< HEAD
from flask import Flask, Response, render_template
import random, json
from listItem import ListItem

=======
from flask import Flask, Response, render_template, jsonify
>>>>>>> ghPages

app = Flask(__name__)


<<<<<<< HEAD
@app.route('/')
def index():
    return render_template("index.html")

=======

@app.route('/') # This is to get the layouts working so that it redirects
def index():
    return render_template("index.html")
>>>>>>> ghPages

@app.route('/saveList')
def saveList():
    lst = []
    with open('localStorage.txt', 'a') as outFile:
        outFile.write(Request.dumps(request.json))

    res = Response('')
    return res

@app.route('/getList')
# read json from file
def getList():
    inFile = open('localStorage.txt', 'r')
    inPut = inFile.read()

    return jsonify(inPut)

<<<<<<< HEAD
=======

>>>>>>> ghPages

if __name__ == '__main__':
    app.run(debug = True, port = 5001)
