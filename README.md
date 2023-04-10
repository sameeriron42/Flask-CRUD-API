# Flask CRUD API
This is a Flask-based CRUD API that allows you to manage users.
## API Reference

#### Get names of all users 

```https
  GET /users
```
Returns a JSON list of names of all users.

#### Get user details by ID

```https
  GET /users/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` |  Id of user to fetch |

The `id` is a ID assigned by MongoDB. API does the converion to ObjectId instance

#### Create a new user

```https
  POST /users
```
#### JOSN PARAMETERS
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `name`      | `string` | Name of the user |
| `email`      | `string`| Email id of user |
| `password`  | `string` | Password of user |

Creates a new user with the specified data. Expects a JSON object representing the new user.

**NOTE:** none of the Parameters are required, everything is set to optional since DB schema is skipped. data validation needs to be done.

#### Update a user

```https
  PUT /users/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` |  **required** Id of user to update |

Updates the user with the specified ID with the new data. Expects a JSON object representing the updated user.

Data must follow same JSON Parameters for POST

### Delete a user
```https
DELETE /users/<id>
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` |  Id of user to DELETE |

Deletes the user with the specified ID.


## Usage/Examples

#### USE postman or curl

Example using **curl**:

### Get all users
```
curl http://localhost:5002/users

[
    "john",
    "johnathon",
    "sameer",
    "rock",
    "sam",
    "koltin"
]
```

### Get user by ID
```
curl http://localhost:5002/users/64300823bd588a12c4acbd80

{
    "name": "koltin",
    "email": "timothy@gmail.com",
    "password": "asUssual"
}
```
### Create a new user
```
curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe", "email":"johndoe@example.com","password":"4321"}' http://localhost:5002/users

{
    "inserted_id": "6430f432c9c293009d54955b"
}
```
### Update a user
```
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Jane Doe", "email":"janedoe@example.com"}' http://localhost:5002/users/6430f432c9c293009d54955b

{
    "name": " Doe",
    "email": "jane@example.com",
    "password": "4321"
}
```
### Delete a user
```
curl -X DELETE http://localhost:5002/users/6430f432c9c293009d54955b

Deleted document with id: 6430f432c9c293009d54955b
```

## Environment Variables
### config.py file

choose URI based on app is ran locally or on docker

`MONGODB_URI` : `mongodb://localhost:27017` or `mongodb://host.docker.internal:27017`

Both the cases Mongo Deamon runs on host.

`COLLECTION_NAME`: name of your collection

### .flaskenv

`FLASK_RUN_PORT` : choose a port different from 5000 to avoid conflicts.

`FLASK_RUN_HOST`: `127.0.0.1` or `0.0.0.0` available externally

### Dockerfile

`EXPOSE` : expose `FLASK_RUN_PORT`'s corresponding port in container.
## Installation


### Clone the repository:
```
git clone https://github.com/sameeriron42/Flask-CRUD-API.git
```
### Install dependencies:
```
pip install -r requirements.txt
```

### Start the server:
run locally on host

``` bash
flask run
```

or on Docker
``` bash
docker build -t flask-app .
docker run -it -p 5002:5002 -d flask-app
```
