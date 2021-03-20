from src.connect_bd.bd import mysql
from flask import request, redirect, flash

class DatabaseModel():
    def lists(self):
        cursor = mysql.get_db().cursor()
        cursor.execute('SHOW DATABASES') 
        data = cursor.close()
        print(data)
        return data

    def create(self, namedb):
        cursor = mysql.get_db().cursor()
        cursor.execute("CREATE DATABASE %s", [namedb])
        mysql.get_db().commit()
        cursor.close()