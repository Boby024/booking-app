from flask import Blueprint, jsonify

user_bp = Blueprint(name="user", import_name=__name__)

@user_bp.route('/login', methods=['GET'])
def login():
    return jsonify({"token": "kjsand923"})

@user_bp.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": ["Alice", "Bob"]})
