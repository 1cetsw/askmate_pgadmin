import database_common


@database_common.connection_handler
def get_title(cursor, name):
    query = """
        SELECT title
        FROM question
        ORDER BY id"""
    cursor.execute(query, {"title": name})
    return cursor.fetchall()

