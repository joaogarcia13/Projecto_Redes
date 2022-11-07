from flask import Flask, request

app = Flask(__name__)

@app.route("/qos", methods=['POST'])
def regras_qos() :
    json = request.json
    print json

    return "ok"