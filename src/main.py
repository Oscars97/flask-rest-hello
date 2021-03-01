"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Personaje, Planet, FavPlanets, FavCharacters
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/people', methods=['GET'])
def handle_hello():
    people_query = Personaje.query.all()
    all_people = list(map(lambda x: x.serialize(), people_query))
    # if user_query is None:
    #     return "Not found", 404
    
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "personajes": all_people
        
    }

    return jsonify(response_body), 200

@app.route('/people/<int:id>', methods=['GET'])
def get_personaje(id):
    personaje = Personaje.query.get(id).serialize()
    # if user_query is None:
    #     return "Not found", 404
    print(personaje)
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "personaje": personaje
        
    }

    return jsonify(response_body), 200



@app.route('/planets/', methods=['GET'])
def get_planets():
    query_planets = Planet.query.all()
    query_planets = list(map(lambda x: x.serialize(), query_planets))
    
    # if user_query is None:
    #     return "Not found", 404
    print(query_planets)
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "planets": query_planets
        
    }

    return jsonify(response_body), 200

@app.route('/users/', methods=['GET'])
def get_todos_usuarios():
    query_users = User.query.all()
    query_users = list(map(lambda x: x.serialize(), query_users))
    
    # if user_query is None:
    #     return "Not found", 404
    print(query_users)
    response_body = {
        "msg": "Hello, this is your GET /user response ",
        "usuarios": query_users
        
    }

    return jsonify(response_body), 200

@app.route('/planet/<int:id>', methods=['GET'])
def get_planet(id):
    planet = Planet.query.get(id)
    if planet is None:
        return "Planet not found", 404
    planet = planet.serialize()
    print(planet)
    # if user_query is None:
    #     return "Not found", 404
    print(planet)
    response_body = {
       
        "planet": planet
        
    }

    return jsonify(response_body), 200   



@app.route('/users/<int:user_id>/favorites', methods=["GET"])
def get_favorites_by_user(user_id):
    user_query = User.query.get(user_id)
    user_planets = user_query.favorites()['planets']
    # if not user_planets:
    #     return jsonify("ERROR"), 404
    user_characters = user_query.favorites()['characters']
    # if not user_characters:
    #     return jsonify("ERROR"), 404
    user_planets = list(map(lambda x: x.serialize(), user_planets))
    user_characters = list(map(lambda x: x.serialize(), user_characters))
    
    if user_query is None:
        return "Planet not found", 404
    
    if user_query is None:
        return "Not found", 404
    response_body = {
        "fav_planets": user_planets,
        "fav_characters": user_characters
        
    }
    

    return jsonify(response_body), 200
    # return jsonify('200'), 200
    


@app.route('/users/<int:user_id>/favorites', methods=['POST'])
def post_favorite(user_id):
    body = request.get_json()
    if body["type"].lower() == "Planet":
        fav = FavPlanets(typeOfFav=body['type'], userId=body['userId'], planetId=body['planetId'], name= body['name'])
        db.session.add(fav)
        db.session.commit()
        response_body = {
       
        "State": "Added"
        
    }
    elif body["type"].lower() == "personaje":
        fav = FavCharacters(typeOfFav=body['type'], userId=body['userId'], characterId=body['characterId'], name= body['name'])
        db.session.add(fav)
        db.session.commit()
        response_body = {
       
        "State": "Added"
        }
    

    return "Ok", 200


@app.route('/users/<int:user_id>/favorites/<int:fav_id>', methods=["DELETE"])
def delete_fav(user_id, fav_id):
    user_query = User.query.get(user_id)
    user_query = user_query.serialize()['characters']
    
    session.query(favplanets).filter(
       favplanets.id==fav_id).delete()

    session.commit()
       
        
    print(user_query, type(user_query))
    # user_query = list(map(lambda x: x.serialize, user_query))
    # for x in user_query:
    #     print(x)
    
    # if user1 is None:
    #     raise APIException('User not found', status_code=404)
    # db.session.delete(user1)
    # db.session.commit()

    return jsonify("Hola"), 200
    # return jsonify('200'), 200
    # this only runs if `$ python src/main.py` is executed

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
