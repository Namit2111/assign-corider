from flask import Blueprint, jsonify, request
from db.schema import mongo
from bson.objectid import ObjectId
from utils.utils import searlize_json
user_bp = Blueprint('get_user', __name__)

# Get all users
@user_bp.route('/users', methods=['GET'])
def get_users():
    users = list(mongo.db.users.find({}, {'password': 0}))
    return searlize_json(data=users), 200

# Get user by ID
@user_bp.route('/users/<id>', methods=['GET'])
def get_user_by_id(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)}, {'password': 0})
    if user:
        return searlize_json(data=user), 200
    return jsonify({"error": "User not found"}), 404
