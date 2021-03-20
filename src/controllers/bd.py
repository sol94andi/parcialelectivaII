from src.models.bd import DatabaseModel
from src import app

databaseModel = DatabaseModel()

class DatabaseController():
    def list(self):        
        data = databaseModel.lists()
        return data

    def create(self, namedb):
        databaseModel.create(namedb)

    def search(self, db):
        data = databaseModel.listTables(db)
        return data
