from playhouse.postgres_ext import *
import json

config_file = open("config.json")
configs = json.load(config_file)

table_name = configs["database_configs"]["table_name"]
host = configs["database_configs"]["host"]
port = configs["database_configs"]["port"]
user = configs["database_configs"]["user"]
password = configs["database_configs"]["password"]

# Connection to the Postgresql database.
try:
    db = PostgresqlDatabase(table_name, host=host, port=port, user=user, password=password)
except Exception as Error:
    db = None
    print("Database connection was not successful: ", Error)

# Class for Meta, all other Models will inherit BaseModel to not have duplicate Meta classes.
class BaseModel(Model):
    class Meta:
        database = db

class Lectures(BaseModel):
    course_id = CharField(max_length=18)
    lecturer = CharField(max_length=255, null=True)
    took = IntegerField(null=True)
    unsuccessful = IntegerField(null=True)
    gpa = DecimalField(null=True, decimal_places=2, max_digits=3, auto_round=False)
    semester = CharField(max_length=30)