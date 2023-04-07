from flask import Flask,Response,request
import json
from pymongo import MongoClient
from bson.objectid import ObjectId
app = Flask(__name__)

@app.route('/')
def home():
    return Response(response=json.dumps({"status":"up"}),status=200,mimetype='application/json')

@app.route('/users', methods=['GET'])
def get_all_users():
    output= user_resource.find({},{"name":1})
    list_of_users = []
    for doc in output:
        list_of_users.append(doc["name"])
    return Response(response=json.dumps(list_of_users),status=200,mimetype='application/json')

@app.get('/users/<id>')
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
def create_user():
    
    data = request.json
    if(data=={}):
        return Response(response='bad request',status=404)
    result = user_resource.insert_one(data)
    if(result.acknowledged==False):
        return Response(status=400)
    output = {'inserted_id':str(result.inserted_id)}

    return Response(response = json.dumps(output),status=200,mimetype='application/json')

@app.put('/users/<id>')
def update(id):
    data = request.json
    user_resource.update_one
    try:
        result = user_resource.update_one({"_id":ObjectId(id)},{'$set':data})
    except Exception as e:
        return Response(response=str(e),status=400,mimetype='text')
    
    if(result.matched_count == 0):
        return Response(response='no record with specified id found',status=400)
    if(result.modified_count == 0):
        return Response(response='no modifications made',status=200)
    
    updatedResult = user_resource.find_one({"_id":ObjectId(id)})
    json_result = {"name": updatedResult['name'],"email":updatedResult['email'],"password":updatedResult['password']}

    return Response(response=json.dumps(json_result),status=200,mimetype='application/json')
    
@app.delete('/users/<id>')
def delete(id):
    try:
        delete_result = user_resource.delete_one({"_id":ObjectId(id)},{})
    except Exception as e:
        return Response(response=str(e),status=400,mimetype='text')
    if(delete_result.deleted_count == 0):
        return Response(response='Nothing to DELETE, no record found with this ID',status=400)

    return Response(response='Deleted document with id: '+id,status=200)



if __name__ == '__main__':
    mongo = MongoClient('localhost',27017)
    db = mongo.test
    user_resource = db['user_resource']
    app.run(debug=True,port=5002,host='0.0.0.0')