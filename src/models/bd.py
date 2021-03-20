from src.connect_bd.bd import mysql
from flask import request, redirect, flash


class DatabaseModel():
    def lists(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("SHOW DATABASES")
        data = cursor.fetchall()
        cursor.close()
        return data

    def create(self, namedb):
        cursor = mysql.get_db().cursor()
        cursor.execute("CREATE DATABASE `%s`" % namedb,)
        mysql.get_db().commit()
        cursor.close()

    def listTables(self, db):
        cursor = mysql.get_db().cursor()
        cursor.execute("SHOW TABLES FROM `%s`" % db)
        search = cursor.fetchall()
        return search
        for i in range(0, len(search)):
            cursor.execute("USE DESCRIBE `%s`" % search[i],)
            data = cursor.fetchall()
            return data[i]
        cursor.close()        

    def createTable(self, nametable):
        cursor = mysql.get_db().cursor()
        cursor.execute("CREATE TABLE dbflask.`%s` (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), address VARCHAR(50), phone VARCHAR(50))" %nametable)
        mysql.get_db().commit()
        cursor.close()
