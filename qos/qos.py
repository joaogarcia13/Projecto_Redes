from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/qos/iniciar", methods=['POST'])
def iniciar_qos() :
    interface = request.json


@app.route("/qos/aplicarRegra", methods=['POST'])
def regras_qos() :
    json = request.json
    

    return "ok"

