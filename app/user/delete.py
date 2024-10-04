from flask import Blueprint, jsonify
from db.schema import mongo
from bson.objectid import ObjectId

user_bp = Blueprint('delete_user', __name__)

@user_bp.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    deleted = mongo.db.users.delete_one({"_id": ObjectId(id)})
    
    if deleted.deleted_count > 0:
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404
