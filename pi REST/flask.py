from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/createwifi", methods=['POST'])
def createwifi():
    name = request.form['name']
    password = request.form['password']
    #chamar script com parametros de entrada
    subprocess.Popen(['nohup','sh', 'createwifi.sh', name, password])
    subprocess.Popen(['nohup','sh','init-network.sh'])
    return "Wifi criada."

@app.route("/setip", methods=['POST'])
def setIP():
    ip = request.form['ip']

    #chamar script

    return "IP definido"

