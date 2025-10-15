#!/usr/bin/python3
from datetime import datetime
from app.models.base_model import BaseModel
import re


class User(BaseModel):
    def __init__(self, first_name, last_name, email, is_admin=False):
        super().__init__()

        if not first_name or len(first_name) > 50:
            raise ValueError("First name is required and must be <= 50 characters.")
        if not last_name or len(last_name) > 50:
            raise ValueError("Last name is required and must be <= 50 characters.")
        if not self._validate_email(email):
            raise ValueError("Invalid email format.")

        self.first_name = first_name
        self.last_name =  last_name
        self.email = email
        self.is_admin = is_admin

    def _validate_email(self, email):
        """Validate email format using regex."""
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None