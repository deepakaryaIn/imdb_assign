import csv
import time
from flask import Blueprint, jsonify, request
from app import mongo
from flask import redirect, url_for

upload_bp = Blueprint('upload', __name__)

# Dummy variable to simulate upload progress
upload_progress = 0

@upload_bp.route('/upload-csv', methods=['POST'])
def upload_csv():
    global upload_progress

    # Check if a file was included in the request
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['file']

    # Check if the file has a valid filename
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    # Handle the CSV upload logic here
    # For demonstration purposes, let's simulate progress
    max_progress = 100
    progress_increment = 10
    num_iterations = max_progress // progress_increment

    for _ in range(num_iterations):
        # Dummy logic to simulate progress
        upload_progress += progress_increment
        time.sleep(0.1)

    # Ensure progress does not exceed maximum
    upload_progress = min(upload_progress, max_progress)

    # Parse the CSV file and insert data into MongoDB
    try:
        file.seek(0)  # Reset file pointer to the beginning
        csv_data = csv.DictReader(file.read().decode('utf-8').splitlines())
        mongo.db.movies.insert_many(csv_data)
    except Exception as e:
        return jsonify({'message': str(e)}), 500

    # Once the upload is complete, redirect to the dashboard page
    return redirect(url_for('view.get_movies'))


@upload_bp.route('/progress', methods=['GET'])
def get_upload_progress():
    # Here, you would retrieve the upload progress from wherever it's stored
    # For example, you might retrieve it from a global variable, database, or session
    global upload_progress
    return jsonify({'progress': upload_progress}), 200

