from flask import Flask,Response,request
import json
from pymongo import MongoClient
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
    return Response(response=json.dumps(list_of_users),status=200,mimetype='appliation/json')

@app.route('/users', methods=['POST'])
def create_user():
    
    data = request.json
    result = user_resource.insert_one(data)
    if(result.acknowledged==False):
        return Response(status=400)
    output = {'inserted_id':str(result.inserted_id)}

    return Response(response = json.dumps(output),status=200,mimetype='application/json')

if __name__ == '__main__':
    mongo = MongoClient('localhost',27017)
    db = mongo.test
    user_resource = db['user_resource']
    app.run(debug=True,port=5002,host='0.0.0.0')