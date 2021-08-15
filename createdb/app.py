from flask import Flask, request, json, jsonify 
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:peacedauda@localhost/apples'
db =SQLAlchemy(app)

class locations(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25))
    longitude = db.Column(db.Float(25))
    latituede = db.Column(db.Float(25))

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.longitude} - {self.latituede}"

@app.route('/')
def index():
    location = locations.query.all()

    output=[]
    for location in location:
        location_data={"latitude": location.latituede, "longitude": location.longitude,  "name": location.name, }

        output.append(location_data)

    return {"Locations": output}

@app.route('/create', methods=["POST"])
def add_location():
        data = json.loads(request.data,strict=False)
        location = locations(name=data['name'], longitude=data['longitude'], latituede=data['latituede'])
        db.session.add(location)
        db.session.commit()
        return jsonify({"your new location has been successfully addeed with" + "id": location.id})


if __name__ == "__main__":
    app.run(debug=True)

