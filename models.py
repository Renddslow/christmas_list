import datetime

from peewee import *

DATABASE = MySQLDatabase("christmas_list", host="localhost", user="root", passwd="littleredunicorns")


class BaseModel(Model):
	class Meta:
		database = DATABASE


class Users(BaseModel):
	user_id = PrimaryKeyField()
	user_name = CharField()
	user_email = CharField(index=True, unique=True)
	user_passwd = CharField()
	user_image_uri = CharField()
	user_invite_code = CharField()
	date_created = DateTimeField(default=datetime.datetime.now())


class Lists(BaseModel):
	list_id = PrimaryKeyField()
	list_name = CharField()
	list_creator_id = IntegerField(index=True)
	list_description = CharField()
	date_created = DateTimeField(default=datetime.datetime.now())


class List_Shares(BaseModel):
	list_share_id = PrimaryKeyField()
	list_id = IntegerField(index=True)
	user_id = IntegerField(index=True)
	date_created = DateTimeField(default=datetime.datetime.now())


class List_Items(BaseModel):
	list_item_id = PrimaryKeyField()
	list_item_name = CharField()
	list_item_description = CharField()
	list_item_url = CharField()
	list_item_image_uri = CharField()
	list_item_purchased = BooleanField(default=False)
	list_item_purchased_by = IntegerField()
	date_created = DateTimeField(default=datetime.datetime.now())
	date_purchased = DateTimeField()


def initialize():
	DATABASE.connect()
	DATABASE.create_tables([Users, Lists,
							List_Shares, List_Items],
							safe=True)
	DATABASE.close()
