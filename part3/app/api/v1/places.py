from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('places', description='Place operations')

place_model = api.model('Place', {
    'title': fields.String(required=True),
    'description': fields.String,
    'price': fields.Float
})

@api.route('/')
class PlaceList(Resource):
    def get(self):
        """Public endpoint: list all places"""
        return facade.get_all_places(), 200

    @jwt_required()
    @api.expect(place_model)
    def post(self):
        """Authenticated: create a new place"""
        current_user = get_jwt_identity()
        data = api.payload
        data['owner_id'] = current_user  # place sahibini token-dən təyin edirik
        new_place = facade.create_place(data)
        return new_place, 201


@api.route('/<place_id>')
class PlaceResource(Resource):
    def get(self, place_id):
        """Public endpoint: get place by id"""
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        return place, 200

    @jwt_required()
    def put(self, place_id):
        """Authenticated: only owner can update"""
        current_user = get_jwt_identity()
        place = facade.get_place(place_id)
        if not place:
            return {"error": "Place not found"}, 404
        if place.owner_id != current_user:
            return {"error": "Unauthorized action"}, 403

        updated = facade.update_place(place_id, api.payload)
        return updated, 200
