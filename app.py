from flask import Flask, jsonify, g

import models

application = Flask(__name__)
application.secret_key = "43dd6b33d467440dbf6153db8cd7ea14"

@application.before_request
def before_request():
	g.db = models.DATABASE
	g.db.connect()

@application.after_request
def after_request(response):
	g.db.close()
	return response

@application.route("/")
def index():
	return jsonify({"message": "Hello World"})


if __name__ == "__main__":
	application.run(host="0.0.0.0", debug=True)
