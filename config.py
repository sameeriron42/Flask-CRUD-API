"""Flask configuration."""
    
TESTING = True
DEBUG = True
FLASK_ENV = 'development'
MONGODB_URI = 'mongodb://host.docker.internal:27017'
COLLECTION_NAME = 'user_resource'