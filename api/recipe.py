class Recipe:
    def get_by_id(id, cursor):
        # make sure the requested id exists in the database
        query = "SELECT * FROM recipes WHERE id = %s"
        cursor.execute(query, (id,))
        return cursor.fetchone()

    def update_recipe(updated_values, cursor, connection):
        query = "UPDATE recipes SET title = %s, portions = %s, ingredients = %s, steps = %s, filters = %s  WHERE id = %s;"
        cursor.execute(query, updated_values)
        connection.commit()

    def insert_recipe(inserted_values, cursor, connection):
        query = "INSERT INTO recipes (title, portions, ingredients, steps, filters) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, inserted_values)
        connection.commit()

    def delete_recipe(id, cursor, connection):
        query = "DELETE FROM user_recipes WHERE recipe_id = %s"
        cursor.execute(query, (id,))
        connection.commit()
        query = "DELETE FROM recipes WHERE id = %s;"
        cursor.execute(query, (id,))
        connection.commit()