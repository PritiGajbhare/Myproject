from config import client
from app import app
from bson.json_util import dumps
from flask import Flask, request, jsonify
import json
import ast

database = client['restfulapi']

collection = database['Student']

print("connection successful")


@app.route('/add', methods=['POST'])

def create_user():

    _json = request.get_json()

    print(_json)

    id=_json['_id']

    name =_json['name']

    _class = _json['class']

    #language = _json['language']

    if request.method =='POST':

        record = {

            "_id":id,

            "name":name,

            "class":_class

        }

        insert_record = collection.insert_one(record)

        return "value is added",200

    else:

        return "value is not added",500



@app.route("/retrive")

def get_display():

    user = collection.find()

    return dumps(user),200



@app.route("/retrive_single/<id>")

def get_single_retrive(id):

    user = collection.find({"_id":id})

    dict ={}

    for x in user:

        dict.update(x)

    return dumps(dict),200



@app.route("/delete/<id>",methods=['DELETE'])

def delete(id):

    user = collection.find({"_id":id})

    _json = request.get_json()

    if user != "" and request.method == 'DELETE':

        collection.delete_one({"_id":id})

        return "user delete successfully"

    else :

        return "unable to delete"



@app.route("/update/<id>",methods=['PUT'])

def update(id):

    _json = request.get_json()

    filter = {'_id':id}

    for x in _json:

        collection.update_one(filter,{"$set":{x:_json[x]}})
    return "value updated", 200

