from flask import Blueprint
from .events.rsvp.user import user_blueprint
from .events.create.plan import create_blueprint
from .events.edit.edit_plan import edit_blueprint
from .events.create.event_routes import event_blueprint

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

api_blueprint.register_blueprint(user_blueprint)
api_blueprint.register_blueprint(create_blueprint)
api_blueprint.register_blueprint(edit_blueprint)
api_blueprint.register_blueprint(event_blueprint)