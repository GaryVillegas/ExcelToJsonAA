from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from excelReading import excel_to_json

#Inicializa la aplicacion flask
app = Flask(__name__)

#Define la carpeta donde se almacenaran temporalmente los archivos subidos
app.config['UPLOAD_FOLDER'] = 'uploads'

#Ruta principal de prueba
@app.route("/")
def home():
    return "API para convertir archivos Excel a JSON"

#Ruta para subir un archivo Excel y recibir su contenido en formato JSON
@app.route("/upload-excel", methods=["POST"])
def upload_excel():
    #Verifica que se haya enviado un en el request
    if 'file' not in request.files:
        return jsonify({'error': 'No se envio ningun archivo'}), 400
    
    file = request.files['file']

    #Verifica que el archivo tenga un nombre valido
    if file.filename == ' ':
        return jsonify({'error': 'El nombre del archivo esta vacio'}), 400
    
    #Asegura que el nombre del archivo sea seguro y lo guarda en el servidor
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    file.save(file_path)

    try:
        #Convierte el archivo excel a json usando la funcion importada
        json_data = excel_to_json(file_path)
        
        #Retorna el json al cliente
        return jsonify(json_data)
    except Exception as e:
        #En caso de error, devuelve el mensaje correspondiente
        return jsonify({'error': str(e)}), 500
    
#Punto de entrada de la aplicacion
if __name__ == '__name__':
    print("Iniciando servidor Flask...")
    app.run(port=5000, debug=True)