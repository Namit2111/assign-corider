from flask_bcrypt import Bcrypt
from bson import json_util
import json

bcrypt = Bcrypt()

def hash_password(password):
    
    return bcrypt.generate_password_hash(password).decode('utf-8')

def check_password(hashed_password, password):
    
    return bcrypt.check_password_hash(hashed_password, password)

def searlize_json(data):
   return json.loads(json_util.dumps(data))