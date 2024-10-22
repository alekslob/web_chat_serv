from flask import Response, jsonify, request
from functools import wraps
from pydantic import ValidationError, BaseModel

from ..exceptions import WebChatApiError, ValidationModelError

def json_response(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if isinstance(result, list):
                return jsonify([model.dict() for model in result])
            elif isinstance(result, dict):
                return jsonify(result)
            else:
                return Response(result.json(), mimetype='application/json')
        except WebChatApiError as e:
            return jsonify({"message": str(e)}), e.status_code
        except Exception as e:
            return jsonify({"message": str(e)}), 400
    return wrapper


def validate(model):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                data = request.get_json()
                kwargs[model.__name__.lower()] = model(**data)
                return func(*args, **kwargs)
            except ValidationError as e:
                raise ValidationModelError(e)
        return wrapper
    return decorator
