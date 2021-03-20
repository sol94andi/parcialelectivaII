from src import app
from src.controllers.bd import DatabaseController
from flask import make_response, jsonify, request

databaseController = DatabaseController()

@app.route('/db', methods=['GET'])
def databaseList():
    dbs = databaseController.list()
    return make_response(jsonify(dbs), 200)

@app.route('/db', methods=['POST'])
def databaseCreate():
    namedb = request.json['namedb']

    databaseController.create(namedb)

    return make_response('Base de datos creada con exito', 201)

@app.route('/tables/<db>', methods=['GET'])
def tableList(db):
    tables = databaseController.search(db)
    return make_response(jsonify(tables), 200)
