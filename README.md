# Flask CRUD API

This is a Flask-based CRUD API that allows you to manage users.
## API Endpoints
### Get all users
`
GET /users
`
Returns a JSON list of all users.

### Get user by ID
`
GET /users/<id>
`
Returns a JSON object representing the user with the specified ID.
The `id` must be string type id assigned by MongoDB. API does the converion to ObjectId instance
### Create a new user
`
POST /users
`
Creates a new user with the specified data. Expects a JSON object representing the new user.

### Update a user
`
PUT /users/<id>
`
Updates the user with the specified ID with the new data. Expects a JSON object representing the updated user.
### Delete a user
`
DELETE /users/<id>
`
Deletes the user with the specified ID.

## Installation

### Clone the repository:
`
git clone https://github.com/sameeriron42/Flask-CRUD-API.git
`
### Install dependencies:
`
pip install -r requirements.txt
`
### Start the server:
`
    flask run
`
## Usage

Once the server is running, you can use a tool like curl or an API client like Postman to make requests to the API endpoints.

Example using curl:

bash

### Get all users
`
curl http://localhost:5000/users
`
### Get user by ID
`
curl http://localhost:5000/users/64300823bd588a12c4acbd80
`
### Create a new user
`
curl -X POST -H "Content-Type: application/json" -d '{"name":"John Doe", "email":"johndoe@example.com","password":"4321"}' http://localhost:5000/users
`
### Update a user
`
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Jane Doe", "email":"janedoe@example.com"}' http://localhost:5000/users/1
`
### Delete a user
`
curl -X DELETE http://localhost:5000/users/64300823bd588a12c4acbd80
`
