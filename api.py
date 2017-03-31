import datetime

from flask import Blueprint, request, jsonify, abort
from flask_restful import (Resource, Api, reqparse,
							inputs, fields, marshal,
							marshal_with, url_for, abort)

import models


class Lists(Resource):
	def __init__(self):
		pass


	def get(self, id):
		user_key = request.args.get("userKey")
		if user_key:
			try:
				user = models.Users.get(user_id = id, user_key = user_key)
			except models.Users.DoesNotExist:
				abort(404)
			else:
				user_id = user.user_id
				user_lists = models.Lists.select()\
									.where(models.Lists.list_creator_id == user_id)\
									.order_by(models.Lists.date_created.desc())

				list_array = []
				for _list in user_lists.execute():
					list_dict = {
						"name": _list.list_name,
						"id": _list.list_id
					}
				return {"lists": list_array}
		else:
			abort(403)


lists_api = Blueprint("api", __name__)
api = Api(lists_api)
api.add_resource(
	Lists,
	'/v1/lists/<int:id>',
	endpoint='lists'
)
