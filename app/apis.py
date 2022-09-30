from flask import Flask, request, jsonify

from app import app, db
from .models import User


@app.route('/api/', methods=['GET'])
def api_hello():
    payload = {
        'method': request.method,
        'message': 'Hello World! This is the REST APIs starter template.'
    }
    return jsonify(payload), 200


@app.route('/api/users', methods=['GET'])
def api_get_users():
    # or users = User.query.all()
    users = db.session.query(User).all()
    result = [{
        'id': user.id,
        'name': user.name,
        'email': user.email
    } for user in users]
    payload = {
        'count': len(result),
        'users': result
    }
    return jsonify(payload), 200


@app.route('/api/user/<int:id>', methods=['GET'])
def api_get_user(id):
    user = User.query.get_or_404(id)
    payload = {
        'id': user.id,
        'name': user.name,
        'email': user.email
    }
    return jsonify(payload), 200


@app.route('/api/add/user', methods=['POST'])
def api_add_user():
    if request.is_json:
        data = request.get_json()
        user = User(name=data['name'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        payload = {
            'message': f'User {user.name} has been created successfully.'
        }
        return jsonify(payload), 201
    else:
        payload = {
            'error': 'The request payload is not JSON format.'
        }
        return jsonify(payload), 404


@app.route('/api/update/user/<int:id>', methods=['POST', 'PUT'])
def api_update_user(id):
    if request.is_json:
        data = request.get_json()
        user = User.query.get_or_404(id)
        user.name = data['name']
        user.email = data['email']
        db.session.commit()
        payload = {
            'message': f'User {user.name} has been updated successfully.'
        }
        return jsonify(payload), 200
    else:
        payload = {
            'error': 'The request payload is not JSON format.'
        }
        return jsonify(payload), 404


@app.route('/api/delete/user/<int:id>', methods=['POST', 'DELETE'])
def api_delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    payload = {
        'message': f'User {user.name} successfully deleted.',
    }
    return jsonify(payload), 200
