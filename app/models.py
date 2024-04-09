from pymongo import TEXT
from app import mongo

# MongoDB schema and indexes
database_schema = {
    "users": {
        "indexes": [
            [("email", TEXT)],  # Text index on the email field for text search
        ],
        "schema": {
            "email": {"type": "str"},
            "password": {"type": "str"},
            # Add more fields as needed (e.g., name, role, etc.)
        }
    },
    "movies": {
        "indexes": [
            [("type", TEXT)],
            [("title", TEXT)],  # Text index on the title field for text search
            [("date_added", TEXT)],
            [("release_year", 1)],
            [("rating", TEXT)],  # Index on the release_date field for sorting
            [("duration", 1)]  # Index on the duration field for sorting
        ],
        "schema": {
            "type": {"type": "str"},
            "title": {"type": "str"},
            "date_added": {"type": "str"},
            "release_year": {"type": "str"},
            "duration": {"type": "int"},
            "rating": {"type": "int"},
            "listed_in": {"type": "list"},
            # Add more fields as needed
        }
    },
    # Add more collections with their respective indexes and schema
}

# Create MongoDB indexes based on the defined schema
def create_indexes():
    for collection, index_info in database_schema.items():
        for index in index_info['indexes']:
            mongo.db[collection].create_index(index)

# Call the function to create indexes when the application starts
create_indexes()
