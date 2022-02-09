import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os # package that interacts with operating system functionality. Needed to interact with environment variables.
from flask import request, jsonify, Flask
from recipe import Recipe
from user import Users
import bcrypt
from flask_cors import CORS
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager

load_dotenv() # a function that reads the .env file and stores those variables in os.env and makes them environment variables

app = Flask(__name__) #creates a flask app 
app.config["DEBUG"] = True

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = os.environ["JWT_TOKEN"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = int(os.environ["JWT_ACCESS_TOKEN_EXPIRES"])
jwt = JWTManager(app)
CORS(app)

def db_connection():
    try:
        # make connection to the database
        connection = mysql.connector.connect(host=os.environ["DB_HOST"],
                                         database=os.environ["DB_NAME"],
                                         user=os.environ["DB_USER"],
                                         password=os.environ["DB_PASS"])
        if connection.is_connected():
            # the cursor is used to execute the queries in the database
            cursor = connection.cursor(dictionary=True)

    except Error as e:
        print("Error while connecting to MySQL", e)
        return None, None, True
        
    return cursor, connection, False

def values_acc(recipe_field):
    if type(recipe_field) != float:        
            try:
                recipe_field = float(recipe_field)         
            except ValueError:
                error_message={"message": "Please insert a number"}
                return jsonify(error_message), 400

@app.route('/api/login', methods=['POST'])
def login():
    user_info = request.json
    if not user_info:
        return "", 400

    email = user_info['email']
    password = user_info['password']

    (cursor, _, has_error) = db_connection()
    if has_error:
        return "", 500

   
    # return the first entry from the database that matches the supplied email
    cursor.execute('SELECT id, password FROM users WHERE email = %s', (email,))
    db_user = cursor.fetchone()

    # if the returned value is None (null) this means that there is no entry with this email in the db
    if db_user is None:
        return "", 400

    # otherwise, we compare the supplied password with the hashed password from the db. if they match,
    # we return the user. otherwise, we return error.
    
    if bcrypt.checkpw(str.encode(password), str.encode(db_user['password'])):
        access_token = create_access_token(identity=db_user["id"])
        return jsonify({"access_token": access_token})

    return "", 400

# make a get route
@app.route('/api/recipes', methods=['GET'])
@jwt_required()
def recipes_all():

    (cursor, _, has_error) = db_connection()
    if has_error:
        return "", 500

    cursor.execute('SELECT * FROM recipes')
    all_recipes = cursor.fetchall()
    
    for recipe_entry in all_recipes:
        recipe_entry["filters"] = recipe_entry["filters"].split(",")

    return jsonify(all_recipes)

# route to add recipes
@app.route('/api/recipes', methods=['POST'])
@jwt_required()
def insert_recipe():

    recipe_info = request.json
    if not recipe_info:
        return "", 400

    recipe_title = recipe_info['title']
    recipe_portions = recipe_info['portions']
    recipe_ingredients = recipe_info['ingredients']
    recipe_steps = recipe_info['steps']
    recipe_filters = ",".join(recipe_info['filters'])

    values_acc(recipe_portions)

    (cursor, connection, has_error) = db_connection()
    if has_error:
        return "", 500

    values=(recipe_title, recipe_portions, recipe_ingredients, recipe_steps, recipe_filters)

    # insert the recipe fields
    Recipe.insert_recipe(values, cursor, connection)
      
    return ""


# route to edit recipes
@app.route('/api/recipes/<recipe_id>', methods=['POST'])
@jwt_required()
def recipe_update(recipe_id):

    (cursor, connection, has_error) = db_connection()
    if has_error:
        return "", 500

    # make sure the requested id exists in the database
    recipe = Recipe.get_by_id(recipe_id, cursor)
    if not recipe:
        return "", 400

    # make sure the request contains data
    recipe_info = request.json
    if not recipe_info:
        return "", 400

    recipe_title = recipe_info["title"] if "title" in recipe_info else recipe["title"]
    recipe_portions = recipe_info["portions"] if "portions" in recipe_info else recipe["portions"]
    recipe_ingredients = recipe_info["ingredients"] if "ingredients" in recipe_info else recipe["ingredients"]
    recipe_steps = recipe_info["steps"] if "steps" in recipe_info else recipe["steps"]
    recipe_filters = recipe_info["filters"] if "filters" in recipe_info else recipe["filters"]
    
    values = (recipe_title, recipe_portions, recipe_ingredients, recipe_steps, recipe_filters, recipe_id)

    values_acc(recipe_portions)

    # update the recipe
    Recipe.update_recipe(values, cursor, connection)
    
    return ""

# route to delete recipes
@app.route('/api/recipes/<recipe_id>', methods=['DELETE'])
@jwt_required()
def recipe_delete(recipe_id):

    (cursor, connection, has_error) = db_connection()
    if has_error:
        return "", 500

    # make sure the requested id exists in the database
    recipe = Recipe.get_by_id(recipe_id, cursor)
    if not recipe:
        return "", 400

    Recipe.delete_recipe(recipe_id, cursor, connection)
      
    return ""

# route to display all recipes for user X
@app.route('/api/user/recipes', methods=['GET'])
@jwt_required()
def user_recipes_all():
    (cursor, _, has_error) = db_connection()
    if has_error:
        return "", 500

    user_id = get_jwt_identity()

    # make sure the requested user id exists in the database
    user = Users.get_by_id(user_id, cursor)
    if not user:
        return "", 404

    # select all the recipes that belong to the user with X user id
    query = "SELECT * FROM recipes WHERE id IN (SELECT recipe_id FROM user_recipes WHERE user_id = %s)"

    cursor.execute(query, (user_id,))
    all_user_recipes = cursor.fetchall()

    return jsonify(all_user_recipes)


# route to delete recipes from user account
@app.route('/api/user/recipes/<recipe_id>', methods=['DELETE'])
@jwt_required()
def user_recipe_delete(recipe_id):

    (cursor, connection, has_error) = db_connection()
    if has_error:
        return "", 500

    user_id = get_jwt_identity()

    # make sure the requested id exists in the database
    query = "SELECT id FROM user_recipes WHERE user_id = %s AND recipe_id = %s"
    cursor.execute(query, (user_id, recipe_id))
    selected_id = cursor.fetchone()

    if not selected_id:
        return "", 400

    query = "DELETE FROM user_recipes WHERE user_id = %s AND recipe_id = %s;"

    cursor.execute(query, (user_id, recipe_id))
    connection.commit()
    
    return ""

# route to add recipes to user account
@app.route('/api/user/recipes/<recipe_id>', methods=['POST'])
@jwt_required()
def user_recipe_add(recipe_id):

    (cursor, connection, has_error) = db_connection()
    if has_error:
        return "", 500

    user_id = get_jwt_identity()

    # make sure the requested id exists in the database
    recipe = Recipe.get_by_id(recipe_id, cursor)
    if not recipe:
        return "", 400
    
    
    # check if the user already owns the recipe
    query = "SELECT recipe_id FROM user_recipes WHERE user_id = %s AND recipe_id = %s"
    cursor.execute(query, (user_id, recipe_id))
    selected_recipe_id = cursor.fetchone()
        
    if selected_recipe_id:
        return jsonify({"message": "You already own this recipe"}), 409
        
    # if no conflict exists, enter it into  user_recipes
    query = "INSERT INTO user_recipes (user_id, recipe_id) VALUES (%s,%s);"

    cursor.execute(query, (user_id, recipe_id))
    connection.commit()
    
    return ""


app.run()