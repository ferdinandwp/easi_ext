from app import app
from flask import flash, request, jsonify, render_template, abort
from db_config import DB_CONN_STR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import ttrf

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/form')
def form():
	return render_template('form.html')

# Add user
@app.route('/add', methods=['POST'])
def add_user():
	try:
		dictJson = request.form.to_dict(flat=True)
		ttrf_obj = ttrf()

		for k in dictJson.keys():
			exec('ttrf_obj.{0} = dictJson[\'{1}\']'.format(k,k))

		result = ttrf_obj.StringToSqlType()

		if result:
			session.add(ttrf_obj)
			session.commit()
			resp = jsonify('User added successfully!')
			resp.status_code = 200
			return resp
		else:
			return unsupported_media_type()
	except Exception as e:
		print(e)
		return str(e)

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
	app.logger.error("Unsupported Media Type: " + request.url + "\rAllowed file types are txt, pdf, png, jpg, jpeg, gif")
	return render_template('415.html'), 415

if __name__ == "__main__":
	try:
		connection = create_engine(DB_CONN_STR)
	except:
		raise Exception("Unable to connect to database")

	Session = sessionmaker(bind=connection)
	session = Session()

	app.run()


