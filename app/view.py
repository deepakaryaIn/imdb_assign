from flask import Blueprint, jsonify, render_template, request
from app import mongo
import pymongo

view_bp = Blueprint('view', __name__)

# @view_bp.route('/movies', methods=['GET'])
# def get_movies():
#     try:
#         # Retrieve query parameters for pagination and sorting
#         page = int(request.args.get('page', 1))
#         per_page = int(request.args.get('per_page', 10))
#         sort_by = request.args.get('sort_by', 'date_added')  # Default sort by date_added
#         order = int(request.args.get('order', 1))  # Default order is ascending

#         # Calculate skip value for pagination
#         skip = (page - 1) * per_page

#         # Retrieve movies data from MongoDB with pagination and sorting
#         movies = mongo.db.movies.find().skip(skip).limit(per_page).sort(sort_by, order)

#         # Count total number of movies (for pagination)
#         total_movies = mongo.db.movies.count_documents({})

#         # Render the dashboard HTML template with movies data
#         return render_template('dashboard.html', movies=movies, total_movies=total_movies, page=page, per_page=per_page), 200
#     except Exception as e:
#         return jsonify({'message': str(e)}), 500
    
@view_bp.route('/movies', methods=['GET'])
def get_movies():
    try:
        page = int(request.args.get('page', 1))
        per_page = int(request.args.get('per_page', 10))
        sort_by = request.args.get('sort', None)
        order = int(request.args.get('order', 1))  # Default order is ascending

        # Get movies from MongoDB, apply sorting if specified
        if sort_by == 'release_year':
            movies = mongo.db.movies.find().sort('release_year', pymongo.ASCENDING)
        elif sort_by == 'duration':
            movies = mongo.db.movies.find().sort('duration', pymongo.ASCENDING)
        elif sort_by == 'date_added':
            movies = mongo.db.movies.find().sort('date_added', pymongo.ASCENDING)
        else:
            movies = mongo.db.movies.find()

        # Count total documents in the collection
        total_movies = mongo.db.movies.count_documents({})

        # Paginate results
        paginated_movies = movies.skip((page - 1) * per_page).limit(per_page)

        return render_template('dashboard.html', movies=paginated_movies, total_movies=total_movies, page=page, per_page=per_page), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500


