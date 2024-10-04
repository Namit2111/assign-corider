from flask import Blueprint, jsonify, request
from db.schema import mongo
from utils.utils import hash_password

user_bp = Blueprint('add_user', __name__)

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data.get('name') or not data.get('email') or not data.get('password'):
        return jsonify({"error": "Missing required fields"}), 400
    
    data['password'] = hash_password(data['password'])
    
    user_id = mongo.db.users.insert_one(data).inserted_id
    return jsonify({"message": "User created", "user_id": str(user_id)}), 201
