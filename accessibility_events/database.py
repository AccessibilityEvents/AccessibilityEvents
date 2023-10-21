# Database model for interacting with the database
# Based on peewee ORM (https://docs.peewee-orm.com/en/latest/)
# Simply import this file to use the database, the tables will be created automatically

import atexit

from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase


PATH = "database.db"
db = SqliteExtDatabase(
    PATH,
    pragmas={"journal_mode": "wal"},
)
atexit.register(lambda: db.close())


class BaseModel(Model):
    class Meta:
        database = db


class Location(BaseModel):
    name = TextField(primary_key=True)
    longitude = FloatField()
    latitude = FloatField()


class Event(BaseModel):
    id = UUIDField(primary_key=True)
    title = TextField()
    description = TextField()
    link = TextField()
    price = TextField()
    tags = TextField()
    start_date = DateTimeField()
    end_date = DateTimeField()
    location = ForeignKeyField(Location)


class EMailContent(BaseModel):
    id = UUIDField(primary_key=True)
    subject = TextField()
    content = TextField()


db.connect()
db.create_tables([Event, Location, EMailContent])
