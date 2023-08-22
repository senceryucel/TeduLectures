import _Database_Models
import json
from playhouse.postgres_ext import *

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
    print("Database connection is successful")
except Exception as Error:
    db = None
    print("Database connection was not successful: ", Error)

Lectures = _Database_Models.Lectures

def table_controller():
    if Lectures.table_exists():
        db.drop_tables([Lectures])
    db.create_tables([Lectures])


def insert_to_lectures(semester, dictionary):
    for i in dictionary:
        course_id = dictionary[i][0]
        lecturer = dictionary[i][1]
        took = int(dictionary[i][2])
        unsuccessful = int(dictionary[i][3])
        gpa = float(dictionary[i][4])
        Lectures.insert(course_id="{}".format(course_id), lecturer="{}".format(lecturer),
                        took="{}".format(took), unsuccessful="{}".format(unsuccessful),
                        gpa="{}".format(gpa), semester="{}".format(semester)).execute()
 