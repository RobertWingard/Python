#model that will connect to mysql

from mysqlconnection import connectToMySQL

DATABASE = 'users_schema'

class User:
    def __init__(self, data): # INPUT ALL DATA IN HERE FROM WHICHEVER TABLE YOU WANT TO USE
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod #target and show all users data
    def get_all(cls):
        query = 'SELECT * FROM users'
        results = connectToMySQL(DATABASE).query_db(query)
        all_users = []
        for u in results:
            all_users.append(cls(u))
        print(all_users)
        return all_users

    @classmethod # shows ONE users data on the next page
    def show_one(cls, data):
        query = 'SELECT * FROM users WHERE id = %(id)s;'
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        print('=================')
        if len(results) > 0:
            user_instance = cls(results[0])
            return user_instance
        return False

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)


    @classmethod # This will allow you to create a new user
    def create(cls, data):
        query = 'INSERT INTO users(first_name, last_name, email) '
        query += 'VALUES (%(first_name)s, %(last_name)s, %(email)s);'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result

    @classmethod # This will allow you to delete a full user from your page
    def delete(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s'
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result



