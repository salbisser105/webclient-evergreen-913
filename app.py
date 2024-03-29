from flask import Flask, request, render_template
import requests

app= Flask(__name__,template_folder='templates')


terrenos_list = ['Planicie','Ladera','Cenagoso','Desértico']

@app.route('/crearSensor',methods= ['GET'])
def crearSensor():
    return render_template('crearSensor.html',terrenos= terrenos_list)

@app.route('/listarSensores',methods = ['GET']) 
def listarSensores():
    predios_list = requests.get('https://api-evergreen-913.azurewebsites.net/tipoSensores').json()
    return render_template('listarSensores.html',sensores = predios_list)

@app.route('/guardarSensor',methods = ['POST'])
def guardarSensor():
    sensor = dict (request.values)
    sensor['area'] = float(sensor['area'])
    requests.post('https://api-evergreen-913.azurewebsites.net/tipoSensores',json = sensor)
    return (listarSensores())

#app.run(port=8000,debug = True)