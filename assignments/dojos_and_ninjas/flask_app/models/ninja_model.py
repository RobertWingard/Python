from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model
from flask_app import app
from flask_app import DATABASE

class Ninja():
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas'
        results = connectToMySQL(DATABASE).query_db(query)
        all_ninjas = []
        for row_from_db in results:
            dojo_instance = cls(row_from_db)
            all_ninjas.append(dojo_instance)
        return all_ninjas

    @classmethod
    def create(cls,data):
        query = 'INSERT INTO ninjas (first_name, last_name, age, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos)s);'
        return connectToMySQL(DATABASE).query_db(query, data)