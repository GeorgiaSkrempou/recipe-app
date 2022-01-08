import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os # package that interacts with operating system functionality. Needed to interact with environment variables.
from flask import request, jsonify, Flask

app = Flask(__name__) #creates a flask app 
app.config["DEBUG"] = True

load_dotenv() # a function that reads the .env file and stores those variables in os.env and makes them environment variables


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
        
    return cursor, connection

def values_acc(recipe_field):
    if type(recipe_field) != float:        
            try:
                recipe_field = float(recipe_field)         
            except ValueError:
                error_message={"message": "Please insert a number"}
                return jsonify(error_message), 400


# make a get route
@app.route('/api/recipes/all', methods=['GET'])
def api_all():

    (cursor, _) = db_connection()

    cursor.execute('SELECT * FROM recipes')
    all_recipes = cursor.fetchall()

    return jsonify(all_recipes)


@app.route('/api/user/recipes', methods=['POST'])
def recipe_update():

    recipe_info = request.json
    if not recipe_info:
        return "", 400

    recipe_title = recipe_info['title']
    recipe_portions = recipe_info['portions']
    recipe_ingredients = recipe_info['ingredients']
    recipe_steps = recipe_info['steps']
    recipe_filters = recipe_info['filters']

    values_acc(recipe_portions)

    query = """
    INSERT INTO recipes (title, portions, ingredients, steps, filters) VALUES (%s, %s, %s, %s, %s)
    """

    values=(recipe_title, recipe_portions, recipe_ingredients, recipe_steps, recipe_filters)

    (cursor, connection) = db_connection()

    cursor.execute(query, values)

    connection.commit()
    
    return ""

app.run()