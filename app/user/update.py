from flask import Blueprint, jsonify, request
from db.schema import mongo
from bson.objectid import ObjectId
from utils.utils import hash_password

user_bp = Blueprint('update_user', __name__)

@user_bp.route('/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    
    if 'password' in data:
        data['password'] = hash_password(data['password'])
    
    updated = mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": data})
    
    if updated.modified_count > 0:
        return jsonify({"message": "User updated"}), 200
    return jsonify({"error": "User not found or no changes made"}), 404
