from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index(): 
    archivos = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', archivos=archivos)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No se seleccionó ningún archivo", 400
    archivo = request.files['file']
    if archivo.filename == '':
        return "No se seleccionó ningún archivo", 400
    archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], archivo.filename))
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
