from flask import Flask, request
import subprocess
import ipaddress
import json

app = Flask(__name__)

@app.route("/createwifi", methods=['POST'])
def createwifi():
    name = request.form['name']
    password = request.form['password']
    interface = request.form['interface']

    if name == "" or password == "":
        return "name ou password vazio."
                
    if (password == "null"):
        subprocess.Popen(['nohup','sh', 'pi_REST/createwifi.sh', name])
    else:
        subprocess.Popen(['nohup','sh', 'pi_REST/createwifi.sh', name, password])

    subprocess.Popen(['nohup', 'sh', 'qos/iniciar.sh', interface])
    subprocess.Popen(['nohup', 'sh', 'firewall/iniciar.sh'])
            
    return "Wifi criada"
            


@app.route("/setip", methods=['POST'])
def setIP():
    ip = request.form['ip']
    subnet = request.form['subnet']
    range1 = request.form['range1']
    range2 = request.form['range2']
    dns = request.form['dns']
    
    try:
        ipaddress.ip_network(ip)
    except:
        return "Erro: ip inválido"
    try:
        ipaddress.ip_network(subnet+"/24")
    except:
        return "Erro: subnet com máscara inválida"
    try:
        ipaddress.ip_network(subnet)
    except:
        return "Erro: subnet inválida"
    try:
        ipaddress.ip_network(range1)
    except:
        return "Erro: range1 inválida"
    try:
        ipaddress.ip_network(range2)
    except:
        return "Erro: range2 inválida"
    try:
        ipaddress.ip_network(dns)
    except:
        return "Erro: dns inválido"
        
    if ipaddress.ip_address(range1) in ipaddress.ip_network(subnet+"/24"):
        return "Erro: ip 0.0.0.0 não é valido"
    
    if ip == "127.0.0.1":
        return "Erro. ip 127.0.0.1 não é válido" 
    
    if ipaddress.ip_address(range1) not in ipaddress.ip_network(subnet+"/24"):
        return "Erro: range1 fora da subnet"
    
    elif ipaddress.ip_address(range2) not in ipaddress.ip_network(subnet+"/24"):
        return "Erro: range2 fora da subnet"

    elif ipaddress.ip_address(range1) > ipaddress.ip_address(range2):
        return "Erro: range1 maior que range2"
    
    else:
        subprocess.Popen(['nohup', 'sh', 'pi_REST/setIP.sh', ip, subnet, range1, range2, dns])

        subprocess.Popen(['nohup','sh','pi_REST/init-network.sh'])

    return "IP definido"

@app.route("/killnetwork", methods=['GET'])
def kill():
    subprocess.Popen(['nohup', 'sh', 'pi_REST/killnetwork.sh'])

    return "Access Point terminado"
    
@app.route("/toggleSwitch", methods=['POST'])
def switchON():
    action = request.form['action']
    if action == "on":
        subprocess.Popen(['nohup', 'sh', 'pi_REST/init-network.sh'])
        return "Interface Switched On"
    if action == "off":
        subprocess.Popen(['nohup', 'sh', 'pi_REST/switchoff.sh'])
        return "Interface Switched Off"
    return "Bad Api Call"
    
@app.route("/getinfo", methods=['GET'])
def getinfo():
    info = subprocess.check_output(['nohup', 'sh', 'pi_REST/getinfo.sh'])
    info_arr = info.decode().split("|")
    outinfo = {"cpu": {"value": str(100-float(info_arr[0])), "units": "%"}, "Memory": {"value":str(float(info_arr[1].split(" ")[1])/1000), "units": "Mb"}, "Temp": {"value": str(float(info_arr[2])/1000), "units":"Cº"}}
    return json.dumps(outinfo)

#QoS
@app.route("/criarRegraQoS", methods=['POST'])
def createRegraQoS():
    interface = request.form['interface']
    name = request.form['name']
    velocidadeRedeBusy = request.form['velocidadeLimitada']
    velocidadeNormal = request.form['velocidadeNormal']

    
    subprocess.Popen(['nohup', 'sh', 'qos/criarRegra.sh', interface, name, velocidadeRedeBusy, velocidadeNormal])

    return "Regra criada"

@app.route("/criarFiltroQoS", methods=['POST'])
def createFiltroQoS():
    interface = request.form['interface']
    filtro = request.form['filtro']
    ip = request.form['ip']

    
    subprocess.Popen(['nohup', 'sh', 'qos/criarFiltro.sh', interface, ip, filtro])

    #outinfo = {"interface": interface, "priority": , "filterHandle": , "filterType": "u32"}

    #return json.dumps(outinfo)
    return "filtro criado"

@app.route("/apagarRegraQoS", methods=['POST'])
def delRegraQoS():
    name = request.form['name']
    
    subprocess.Popen(['nohup', 'sh', 'qos/apagarRegra.sh', name])

    return "Regra apagada"

@app.route("/apagarFiltroQoS", methods=['POST'])
def delFiltroQoS():
    interface = request.form['interface']
    priority = request.form['priority']
    filterHandle = request.form['filterHandle']
    filterType = request.form['filterType']

    subprocess.Popen(['nohup', 'sh', 'qos/apagarFiltro.sh', interface, priority, filterHandle, filterType])

    return "Filtro apagado"


#Firewall
@app.route("/criarRegraFirewall", methods=['POST'])
def criarRegraFirewall():
    interface = request.form['interface']
    tipo = request.form['tipo']
    ipPort = request.form['ipPort']

    subprocess.Popen(['nohup', 'sh', 'firewall/criarRegra.sh', interface, tipo, ipPort])

    return "Regra criada"

@app.route("/apagarRegraFirewall", methods=['POST'])
def apagarRegraFirewall():
    interface = request.form['interface']
    tipo = request.form['tipo']
    ipPort = request.form['ipPort']

    subprocess.Popen(['nohup', 'sh', 'firewall/criarRegra.sh', interface, tipo, ipPort])

    return "Regra apagada"

#Monitoring
@app.route("/monitoring", methods=['POST'])
def monitoring() :
    interface = request.form['interface']

    device = subprocess.check_output(['nohup', 'sh', 'networkManager/monitoring.sh', interface])

    return str(device)

#Manutenção
@app.route("/update", methods=['GET'])
def updatePi() :
    subprocess.Popen(['nohup', 'sh', 'updatePi.sh'])

    return "Already update."