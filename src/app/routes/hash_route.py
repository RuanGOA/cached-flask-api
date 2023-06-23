import json
import base64

from flask import Blueprint, Response, request
from flask_api import status as http_status

route_hash = Blueprint('hash', __name__)


@route_hash.route('/<item_id>', methods=['GET'])
def hash_text(item_id):
    text_bytes = item_id.encode("ascii")
    text_based_bytes = base64.b64encode(text_bytes)
    body = { "encoded": text_based_bytes.decode("ascii") }
    
    return Response(
        json.dumps(body),
        status=http_status.HTTP_200_OK,
        mimetype='application/json'
    )
