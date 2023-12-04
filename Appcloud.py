from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Dossier où les images seront stockées
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Récupérer la liste des fichiers dans le dossier uploads
    image_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f))]
    return render_template('index.html', image_files=image_files)

# ...

@app.route('/view_album')
def view_album():
    # Récupérer la liste des fichiers dans le dossier uploads
    image_files = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], f))]
    return render_template('album.html', image_files=image_files)

# ...

@app.route('/upload', methods=['POST'])
def upload_file():
    # Vérifier si la requête contient un fichier
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    # Vérifier si le fichier est vide
    if file.filename == '':
        return redirect(request.url)

    # Vérifier si le fichier est une image
    if file and allowed_file(file.filename):
        # Enregistrer le fichier dans le dossier uploads
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
        return redirect(url_for('index'))

    return redirect(request.url)

def allowed_file(filename):
    # Vérifier si l'extension du fichier est autorisée
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

if __name__ == '__main__':
    # Démarrer l'application Flask
    app.run(debug=True)
