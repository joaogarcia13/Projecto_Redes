from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/createwifi", methods=['POST'])
def createwifi():
    name = request.form['name']
    password = request.form['password']
    if (password == "null"):
        subprocess.Popen(['nohup','sh', 'pi_REST/createwifi.sh', name])
    else:
        subprocess.Popen(['nohup','sh', 'pi_REST/createwifi.sh', name, password])
    
    return "Wifi criada"

@app.route("/setip", methods=['POST'])
def setIP():
    ip = request.form['ip']
    subnet = request.form['subnet']
    range1 = request.form['range1']
    range2 = request.form['range2']
    dns = request.form['dns']

    subprocess.Popen(['nohup', 'sh', 'pi_REST/setIP.sh', ip, subnet, range1, range2, dns])

    subprocess.Popen(['nohup','sh','pi_REST/init-network.sh'])

    return "IP definido"

@app.route("/killnetwork", methods=['GET'])
def kill():
    subprocess.Popen(['nohup', 'sh', 'pi_REST/killnetwork.sh'])

    return "Access Point terminado"
    
@app.route("/OnOffSwitch", methods=['POST'])
def switchON():
    action = request.form['action']
    if action == "on":
        subprocess.Popen(['nohup', 'sh', 'pi_REST/init-network.sh'])
        return "Interface Switched On"
    if action == "off":
        subprocess.Popen(['nohup', 'sh', 'pi_REST/switchoff.sh'])
        return "Interface Switched Off"
    return "Bad Api Call"


#QoS
@app.route("/iniciarQoS", methods=['POST'])
def iniciar_qos() :
    interface = request.form['interface']

    subprocess.Popen(['nohup', 'sh', 'qos/iniciar.sh', interface])

    return "QoS iniciado"


@app.route("/criarRegraQoS", methods=['POST'])
def createRegraQoS():
    interface = request.form['interface']
    name = request.form['name']
    velocidadeRedeBusy = request.form['velocidadeLimitada']
    velocidadeNormal = request.form['velocidadeNormal']

    
    subprocess.Popen(['nohup', 'sh', 'qos/criarRegra.sh', interface, name, velocidadeRedeBusy, velocidadeNormal])

    return "Regra criada"

@app.route("/apagarRegraQoS", methods=['POST'])
def delRegraQoS():
    name = request.form['name']
    
    subprocess.Popen(['nohup', 'sh', 'qos/apagarRegra.sh', name])

    return "Regra apagada"

@app.route("/verRegraQoS", methods=['POST'])
def showRegraQoS():
    name = request.form['name']
    
    regras = subprocess.check_output(['nohup', 'sh', 'qos/verRegras.sh', name])

    return str(regras)

@app.route("/criarFiltroQoS", methods=['POST'])
def createFiltroQoS():
    interface = request.form['interface']
    filtro = request.form['filtro']
    ip = request.form['ip']

    
    subprocess.Popen(['nohup', 'sh', 'qos/criarFiltro.sh', interface, ip, filtro])

    return "Filtro criado"

#Monitoring
@app.route("/monitoring", methods=['POST'])
def monitoring() :
    interface = request.form['interface']

    device = subprocess.check_output(['nohup', 'sh', 'networkManager/monitoring.sh', interface])

    return str(device)
