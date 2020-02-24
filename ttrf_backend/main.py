from app import app
from flask import jsonify
from flask import flash, request
from db_config import DB_CONN_STR
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from schema import ttrf

# Add user
@app.route('/add', methods=['POST'])
def add_user():
	try:
		dictJson = request.form.to_dict(flat=True)
		ttrf_obj = ttrf()

		for k in dictJson.keys():
			exec('ttrf_obj.{0} = dictJson[\'{1}\']'.format(k,k))

		ttrf_obj.StringToSqlType()

		session.add(ttrf_obj)
		session.commit()
		resp = jsonify('User added successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)

# Display all users
@app.route('/describe')
def describe_users():
	try:
		keyList = list(session.query(ttrf).first().serialize().keys())
		resp = jsonify(keyList)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)

# Display contents of table
@app.route('/contents')
def users():
	try:
		mergedList = []
		keyList = list(session.query(ttrf).first().serialize().keys())
		mergedList.append(keyList)
		for instance in session.query(ttrf).all():
			valueList = list(instance.serialize().values())
			mergedList.append(valueList)
		resp = jsonify(mergedList)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)

'''
# display given user
@app.route('/user/<int:id>')
def user(id):
	try:
		test = session.query(ttrf).filter_by(id=id).first().serialize()
		print(test)
		resp = jsonify(test)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)


# Update given user
@app.route('/update', methods=['POST'])
def update_user():
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		_json = request.json
		_id = _json['id']
		_name = _json['user_name']
		_email = _json['user_email']
		_password = _json['user_password']
		# validate the received values
		if _name and _email and _password and _id and request.method == 'POST':
			# save edits
			sql = "UPDATE ttrf SET user_name=%s, user_email=%s, user_password=%s WHERE id=%s"
			data = (_name, _email, _hashed_password, _id,)
			cursor.execute(sql, data)
			conn.commit()
			resp = jsonify('User updated successfully!')
			resp.status_code = 200
			return resp
		else:
			return not_found()
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()

# Delete given user
@app.route('/delete/<int:id>')
def delete_user(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM ttrf WHERE id=%s", (id,))
		conn.commit()
		resp = jsonify('User deleted successfully!')
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
'''
# Error handler
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
	try:
		connection = create_engine(DB_CONN_STR)
	except:
		raise Exception("Unable to connect to database")

	Session = sessionmaker(bind=connection)
	session = Session()

	app.run()


