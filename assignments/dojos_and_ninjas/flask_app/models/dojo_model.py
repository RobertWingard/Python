from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models.ninja_model import Ninja 

class Dojo():
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos'
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = []
        for row_from_db in results:
            dojo_instance = cls(row_from_db)
            all_dojos.append(dojo_instance)
        return all_dojos

    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);" #<--- this one needs to match controller route
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod
    def get_dojo_and_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results =connectToMySQL(DATABASE).query_db(query,data)
        if not results:
            return False
        dojo_instance = cls(results[0])
        ninjas = []
        for ninja_db in results:
            data = {
                **ninja_db,
                'id': ninja_db['ninjas.id'],
                'created_at': ninja_db['ninjas.created_at'],
                'updated_at': ninja_db['ninjas.updated_at'],
            }
            ninjas.append(Ninja(data))
        dojo_instance.apples = ninjas
        return dojo_instance
            


