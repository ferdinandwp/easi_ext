from flask import Flask

UPLOAD_FOLDER = 'uploaded_file'
ALLOWED_EXTENSIONS = set(['pdf', 'xlsx', 'xlsm', 'xls', 'csv'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024