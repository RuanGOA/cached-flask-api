from app.routes.status_route import status
from app.routes.hi_route import hi
from app.routes.hash_route import route_hash

def create_routes(app):
    app.register_blueprint(status, url_prefix='/status')
    app.register_blueprint(hi, url_prefix='/hi')
    app.register_blueprint(route_hash, url_prefix='/hash')
