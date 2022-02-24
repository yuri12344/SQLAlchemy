from flask import Blueprint, request, current_app, session
from app.models.states_model import StateModel

bp_create_state = Blueprint("bp_create_state", __name__)

@bp_create_state.route("/states", methods=["POST"])
def create_state():
    session = current_app.db.session

    data = request.get_json()

    state = StateModel(**data)

    session.add(state)
    session.commit()

    return {
        "id": state.id,
        "name": state.name,
        "acronym": state.acronym,
        "population": state.population,
        "area": float(state.area)
    }