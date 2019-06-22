
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def getRequest():

    data = request.get_json()
    print(data)
    return jsonify(data)

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5000,debug=True)
