import functools
from flask import request
from ..models.user import User

def api_key_required(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs): 
        api_key = request.headers.get("api-key")

        if not api_key:
            return {"message": "Please provide an API key"}, 403
        
        user = User.query.filter_by(api_key= api_key).first()

        if not user:
            return {"message": "Invalid API key credentials provided"}, 403
        
        return func(*args, **kwargs)
    return decorator