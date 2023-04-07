from flask import Flask,Response,request
import json
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.config.from_pyfile('config.py')
mongo = MongoClient(app.config['MONGODB_URI'])
db = mongo.test
user_resource = db[app.config['COLLECTION_NAME']]

@app.route('/')
def home():
    return Response(response=json.dumps({"status":"up"}),status=200,mimetype='application/json')

@app.route('/users', methods=['GET'])
#returns names of all users in database
def get_all_users():
    output= user_resource.find({},{"name":1})
    list_of_users = []
    for doc in output:
        list_of_users.append(doc["name"])
    return Response(response=json.dumps(list_of_users),status=200,mimetype='application/json')

@app.get('/users/<id>')
#returns document associated with <id>
def get_user(id):
    try:
        result = user_resource.find_one({"_id": ObjectId(id)})
        if result is None:
            raise Exception("no record found!!")
    except Exception as e:
        return Response(response=str(e),status=400,mimetype='text')
    else:
        json_result = {"name": result['name'],"email":result['email'],"password":result['password']}
        return Response(response=json.dumps(json_result),status=200,mimetype='application/json')

@app.route('/users', methods=['POST'])
#create new document
def create_user():
    data = request.json
    #skipping data validation as DB schema is missing
    if(data=={}):
        return Response(response='Bad request, data cannot be empty',status=404)

    result = user_resource.insert_one(data)
    if(result.acknowledged==False):
        return Response(status=404)
    output = {'inserted_id':str(result.inserted_id)}

    return Response(response = json.dumps(output),status=201,mimetype='application/json')

@app.put('/users/<id>')
def update(id):
    data = request.json
    user_resource.update_one
    try:
        result = user_resource.update_one({"_id":ObjectId(id)},{'$set':data})
    except Exception as e:
        return Response(response=str(e),status=400,mimetype='text')
    
    if(result.matched_count == 0):
        return Response(response='no record with specified id found',status=404)
    if(result.modified_count == 0):
        return Response(response='no modifications made',status=200)
    
    updatedResult = user_resource.find_one({"_id":ObjectId(id)})
    json_result = {"name": updatedResult['name'],"email":updatedResult['email'],"password":updatedResult['password']}

    return Response(response=json.dumps(json_result),status=201,mimetype='application/json')
    
@app.delete('/users/<id>')
def delete(id):
    try:
        delete_result = user_resource.delete_one({"_id":ObjectId(id)})
    except Exception as e:
        return Response(response=str(e),status=400,mimetype='text')
    if(delete_result.deleted_count == 0):
        return Response(response='Nothing to DELETE, no record found with this ID',status=404)

    return Response(response='Deleted document with id: '+id,status=200)



