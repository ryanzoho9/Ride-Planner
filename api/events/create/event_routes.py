from flask import Blueprint, jsonify, request
import json
from api.events.rsvp.event_userAll import get_events, event_allUser

event_blueprint = Blueprint('event', __name__, url_prefix='/events/create')

@event_blueprint.route('/get_event', methods=['GET'])
def get_event():
    """
    Fetch single event details by eventId (event_uuid).
    """
    data = get_events(request.args.get('eventId'))

    # If data is a dict containing an error, handle it
    if isinstance(data, dict) and "error" in data:
        return jsonify(data), 500
    
    # Otherwise, `data` is a JSON string of an array of events
    events_list = json.loads(data)
    if not events_list:
        return jsonify({"error": "Event not found"}), 404
    
    # We assume there's only one event matching eventId
    return events_list[0], 200

@event_blueprint.route('/get_event_attendees', methods=['GET'])
def get_event_attendees():
    """
    Fetch all attendees for a given eventId (event_uuid).
    """
    data = event_allUser(request.args.get('eventId'))

    # If data is a dict containing an error, handle it
    if isinstance(data, dict) and "error" in data:
        return jsonify(data), 500

    # Otherwise, data is a JSON string
    attendees_list = json.loads(data)
    return jsonify(attendees_list), 200
