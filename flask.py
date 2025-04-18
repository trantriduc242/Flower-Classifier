from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os

# Initialize Flask app
app = Flask(__name__)

# Set a folder to store uploaded files
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Check if the file is an allowed image type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route to display the upload page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file upload and processing
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Here you can integrate your image processing code (your project logic)
        # processed_image = your_image_processing_function(filepath)

        # Assuming the processed image is saved as 'processed_image.png'
        processed_image = 'path_to_processed_image.png'

        return send_file(processed_image, mimetype='image/png')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
