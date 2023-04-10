from flask import Flask
from resources.user_bp import user 

app = Flask(__name__)
app.config.from_pyfile('config.py')

app.register_blueprint(user)

