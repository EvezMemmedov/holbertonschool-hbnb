from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('users', description='User operations')

user_update_model = api.model('UserUpdate', {
    'first_name': fields.String,
    'last_name': fields.String
})

@api.route('/<user_id>')
class UserResource(Resource):
    @jwt_required()
    @api.expect(user_update_model)
    def put(self, user_id):
        """Authenticated: user can only update own data"""
        current_user = get_jwt_identity()
        if current_user != user_id:
            return {"error": "Unauthorized action"}, 403

        data = api.payload
        if "email" in data or "password" in data:
            return {"error": "You cannot modify email or password"}, 400

        updated = facade.update_user(user_id, data)
        return updated, 200
