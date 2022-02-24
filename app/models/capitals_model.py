from app import db

class CapitalsModel(db.Model):
    __tablename__ = 'capitals'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    neighborhoods = db.Column(db.String(255))
    population = db.Column(db.Integer)

    # Here i appoint to the State
    state_id = db.Column(db.Integer, db.ForeignKey("states.id"), nullable=False)
    # And here, i can take the State, inside of the object CapitalModel, like join and where
    state = db.relationship('StateModel', backref=db.backref("capitals", uselist=True))


    def __init__(self, name, neighborhoods, population, state_id):
        self.name = name
        self.neighborhoods = neighborhoods
        self.population = population
        self.state_id = state_id
    
