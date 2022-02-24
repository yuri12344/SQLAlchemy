from app import db


class StateModel(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, primary_key=True)
    
    name = db.Column(db.String(50), nullable=False)
    acronym = db.Column(db.String(2), nullable=False)
    population = db.Column(db.Integer)
    area = db.Column(db.DECIMAL)

    def __init__(self, name, acronym, population, area):
        self.name = name
        self.acronym = acronym
        self.population = population
        self.area = area