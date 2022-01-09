class Users:
    def get_by_id(id, cursor):
        # make sure the requested id exists in the database
        query = "SELECT id FROM users WHERE id = %s"
        cursor.execute(query, (id,))
        return cursor.fetchone()

    def user_get_recipes():
        pass