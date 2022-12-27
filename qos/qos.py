from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/iniciarQoS", methods=['POST'])
def iniciar_qos() :
    interface = request.form['interface']

    subprocess.Popen(['nohup', 'sh', 'QoS/iniciarQoS.sh', interface])

    return "QoS iniciado"


@app.route("/criarRegra", methods=['POST'])
def createwifi():
    interface = request.form['interface']
    name = request.form['name']
    velocidade = request.form['velocidade']

    
    subprocess.Popen(['nohup', 'sh', 'QoS/criarRegra.sh', interface, name, velocidade+10, velocidade])

    return "Regra criada"

