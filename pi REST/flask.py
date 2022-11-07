from flask import Flask, request

app = Flask(__name__)

@app.route("/createwifi", methods=['POST'])
def createwifi():
    name = request.POST['name']
    password = request.POST['password']

    #chamar script com parametros de entrada

    return "Wifi criada."

@app.route("/setip", methods=['POST'])
def setIP() :
    ip = request.POST('ip')

    #chamar script

    return "IP "
