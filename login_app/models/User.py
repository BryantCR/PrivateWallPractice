from login_app.config.MySQLConnection import connectToMySQL
from login_app import app 
from datetime import date, datetime
from flask import flash

#compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, users_id, first_name, last_name, email, users_password, created_at):
        self.users_id = users_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.users_password = users_password
        self.created_at = created_at

    @classmethod
    def register_login(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, users_password, created_at, updated_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s, %(encryptedpassword)s, SYSDATE(), SYSDATE());"
        data2 = {
            "first_name" : data[0],
            "last_name" : data[1],
            "email" : data[2],
            "users_password" : data[3],
            "encryptedpassword" : data[4],
            "confirm_users_password" : data[5]
        }
        result = connectToMySQL('login_and_registration').query_db( query, data2 )
        return result
    
    @classmethod
    def user_login(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data2 = {
            "email" : data[0],
            "users_password" : data[1],
        }
        result = connectToMySQL('login_and_registration').query_db( query, data2 )
        return result

















############################################################################################################## STATIC METHOD
    @staticmethod
    def validate_user_password( data ):

        isValid = True
        if len( first_name ) < 5:
            flash( "Username must be at least 5 characters long" )
            isValid = False 
        if len( last_name ) < 5:
            flash( "Username must be at least 5 characters long" )
            isValid = False
        if len( email ) < 5:
            flash( "Username must be at least 5 characters long" )
            isValid = False 
        if len( users_password ) < 8:
            flash( "Password must be at least 8 characters long")
            isValid = False
        
        return isValid






    # @classmethod
    # def get_all_users(cls):
    #     query = "SELECT * FROM users;"
    #     results = connectToMySQL("users_shema").query_db( query )
    #     users = []
    #     for n in results:
    #         users.append( User( n['id'], n['first_name'], n['last_name'], n['email'], n['created_at'] ) )
    #     return users
    
    # @classmethod
    # def addDataForm(cls, data):
    #     query = "INSERT INTO users (first_name , last_name , email, created_at, updated_at) VALUES ( %(first_name)s , %(last_name)s , %(email)s, SYSDATE(), SYSDATE());"
    #     result = connectToMySQL('users_shema').query_db(query,data)
    #     return result

    # @classmethod
    # def editUserData(cls, data):
    #     query = "UPDATE users SET first_name = %(first_name2Fromform2)s, last_name = %(lastst_name2Fromform2)s, email = %(email2Fromform2)s, updated_at = SYSDATE() WHERE id=%(id)s;"
    #     result = connectToMySQL('users_shema').query_db(query, data)
    #     print(data)
    #     return result

    # @classmethod
    # def get_one(cls, id):
    #     print("8")
    #     query  = "SELECT * FROM users WHERE id = %(id)s;"
    #     data = {
    #         "id" : id
    #     }
    #     result = connectToMySQL('users_shema').query_db( query, data )
    #     user_data = []

    #     #for users in result:
    #         #user_data.append(User(user['id'],user['first_name'], user['last_name'], user['email'],user['created_at'],user['updated_at']))
    #     print("9", user_data )
    #     return result

    # @classmethod
    # def deleteUser(cls, data ):
    #     query = "DELETE FROM users WHERE id = %(id)s;"
    #     return connectToMySQL('users_shema').query_db( query, data )