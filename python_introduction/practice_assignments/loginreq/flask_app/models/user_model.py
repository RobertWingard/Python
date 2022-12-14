from flask_app.config.mysqpconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.password = data['password']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, password, email) VALUES (%(first_name)s, %(last_name)s, %(password)s, %(email)s);"
        return connectToMySQL(DATABASE). query_db(query,data)


    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])



    @staticmethod
    def validate(user_data):
        is_valid = True
        if len(user_data['first_name']) < 2:
            flash('First name required, please make at least 2 characters long ', 'reg')
            is_valid = False
        if len(user_data['last_name']) < 2:
            flash('Last name required, please enter at least 2 characters.', 'reg')
            is_valid = False
        if len(user_data['email']) < 1:
            flash('Email required', 'reg')
            is_valid = False
        elif not EMAIL_REGEX.match(user_data['email']):
            flash('Invalid email format', 'reg')
            is_valid = False
        else:
            data = {
                'email': user_data['email']
            }
            potential_user = User.get_by_email(data)
            if potential_user:
                flash('email already registered', 'reg')
                is_valid = False
        if len(user_data['password']) < 8:
            flash('password must be at least 8 characters long.', 'reg')
            is_valid = False
        elif not user_data['password'] == user_data['confirm_pass']:
            flash('passes dont match', 'reg')
            is_valid = False
        return is_valid

