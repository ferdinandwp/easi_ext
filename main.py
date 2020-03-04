import os
import urllib.request
from app import app, UPLOAD_FOLDER, allowed_file
from flask import flash, request, jsonify, render_template, abort, redirect
from db_config import DB_CONN_STR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import ttrf
from werkzeug.utils import secure_filename
from datetime import datetime

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/form')
def form():
	return render_template('form.html')

@app.route('/success')
def success():
	return render_template('success.html')

# Add user
@app.route('/add', methods=['POST'])
def add_user():
	try:
		# file upload request
		if 'file' not in request.files:
			error_message = 'Error: No file field defined in request'
			print(error_message)
			resp = jsonify(error_message)
			resp.status_code = 200
			return resp
		file = request.files['file']

		if file and allowed_file(file.filename):
			if os.path.exists(UPLOAD_FOLDER):
				fullFilename = secure_filename(file.filename)
				filename, fileExtension = os.path.splitext(fullFilename)
				newName = filename + '_' + datetime.now().strftime("%Y%m%d%H%M%S") + fileExtension
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
			else:
				raise ValueError("Specified path in server doesn't exist")

		# form submit request
		dictJson = request.form.to_dict(flat=True)
		ttrf_obj = ttrf()
		for k in dictJson.keys():
			exec('ttrf_obj.{0} = dictJson[\'{1}\']'.format(k,k))

		# Convert string type to correspondent types
		ttrf_obj.StringToSqlType()

		# Add and commit session to update database
		session.add(ttrf_obj)
		session.commit()
		return redirect('/success')
		
	except Exception as e:
		print(e)
		return unsupported_media_type(e)

# Error handler
@app.errorhandler(404)
def not_found(error=None):
	app.logger.error('Page not found: %s', (request.path))
	return render_template('404.html'), 404

@app.errorhandler(413)
def request_entity_too_large(error=None):
	app.logger.error("Request entity too large: " + request.url)
	return render_template('413.html'), 413

@app.errorhandler(415)
def unsupported_media_type(error=None):
	app.logger.error("Unsupported Media Type: " + request.url + "\rThe only allowed file types are xlsx, xlsm, xls, csv, pdf")
	return render_template('415.html'), 415

@app.errorhandler(501)
def unsupported_media_type(error=None):
	return render_template('501.html', error=error), 501

if __name__ == "__main__":
	try:
		connection = create_engine(DB_CONN_STR)
	except:
		raise Exception("Unable to connect to database")

	Session = sessionmaker(bind=connection)
	session = Session()

	app.run()


