from src.models.bd import DatabaseModel
from src import app

class DatabaseController():
    def list(self):
        databaseModel = DatabaseModel()
        data = databaseModel.lists()

        return data

    def create(self, namedb):
        databaseModel = DatabaseModel()
        databaseModel.create(namedb) 
