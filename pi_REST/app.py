from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/createwifi", methods=['POST'])
def createwifi():
    name = request.form['name']
    password = request.form['password']
    if (password == "null"):
        subprocess.Popen(['nohup','sh', 'createwifi.sh', name])
    else:
        subprocess.Popen(['nohup','sh', 'createwifi.sh', name, password])
    
    return "Wifi criada"

@app.route("/setip", methods=['POST'])
def setIP():
    ip = request.form['ip']
    subnet = request.form['subnet']
    range1 = request.form['range1']
    range2 = request.form['range2']
    dns = request.form['dns']

    subprocess.Popen(['nohup', 'sh', 'setIP.sh', ip, subnet, range1, range2, dns])

    subprocess.Popen(['nohup','sh','init-network.sh'])

    return "IP definido"

@app.route("/killnetwork", methods=['GET'])
def kill():
    subprocess.Popen(['nohup', 'sh', 'killnetwork.sh'])

    return "Access Point terminado"
    
@app.route("/switchOn", methods=['GET'])
def switchON():
    subprocess.Popen(['nohup', 'sh', 'init-network.sh'])
    
    return "Interface Switched On"
    
@app.route("/switchOff", methods=['GET'])
def switchOFF():
    subprocess.Popen(['nohup', 'sh', 'switchoff.sh'])
    
    return "Interface Switched Off"
