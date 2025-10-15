#!/usr/bin/python3
from app.models.base_model import BaseModel


class Rewiew(BaseModel):
    def __init__(self, text, user, rating, place):
        super().__init__()

        if not text:
            raise ValueError("Text is required.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        
        self.text = text
        self.user = user
        self.rating = rating
        self.place = place
