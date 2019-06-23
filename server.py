from main import main
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def getRequest():

    data = request.get_json()
    res =  main(data)
    return res


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=8000,debug=True)
