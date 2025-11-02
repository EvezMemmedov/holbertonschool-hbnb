from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.services import facade

api = Namespace('reviews', description='Review operations')

review_model = api.model('Review', {
    'place_id': fields.String(required=True),
    'text': fields.String(required=True)
})

@api.route('/')
class ReviewList(Resource):
    @jwt_required()
    @api.expect(review_model)
    def post(self):
        """Create a new review (authenticated only)"""
        current_user = get_jwt_identity()
        data = api.payload
        place = facade.get_place(data['place_id'])

        if not place:
            return {"error": "Place not found"}, 404

        if place.owner_id == current_user:
            return {"error": "You cannot review your own place"}, 400

        existing = facade.get_review_by_user_and_place(current_user, data['place_id'])
        if existing:
            return {"error": "You have already reviewed this place"}, 400

        data['user_id'] = current_user
        review = facade.create_review(data)
        return review, 201


@api.route('/<review_id>')
class ReviewResource(Resource):
    @jwt_required()
    def put(self, review_id):
        """Update review (only by owner)"""
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        if review.user_id != current_user:
            return {"error": "Unauthorized action"}, 403

        updated = facade.update_review(review_id, api.payload)
        return updated, 200

    @jwt_required()
    def delete(self, review_id):
        """Delete review (only by owner)"""
        current_user = get_jwt_identity()
        review = facade.get_review(review_id)
        if not review:
            return {"error": "Review not found"}, 404
        if review.user_id != current_user:
            return {"error": "Unauthorized action"}, 403

        facade.delete_review(review_id)
        return {"message": "Review deleted successfully"}, 200
