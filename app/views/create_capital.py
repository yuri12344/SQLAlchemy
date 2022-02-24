from flask import Blueprint, request, current_app, session
from app.models.capitals_model import CapitalsModel
from app.models.states_model import StateModel
import ipdb

bp_create_capital = Blueprint("bp_create_capital", __name__)

@bp_create_capital.route("/capitals", methods=["POST"])
def create_capials():
    session = current_app.db.session

    data = request.get_json()
    estado = StateModel.query.filter_by(name=data["state_name"]).first()

    data.pop("state_name")
    data["state_id"] = estado.id

    capital = CapitalsModel(**data)

    session.add(capital)
    session.commit()
    
    return {
        "id": capital.id,
        "name": capital.name,
        "neighborhoods": capital.neighborhoods,
        "population": capital.population,
        "state_name": capital.state.name
    }