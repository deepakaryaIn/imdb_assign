# IMDB Project

This project is a Flask application for managing movie data using MongoDB. It includes features for user authentication, CSV upload, and viewing movies data with pagination and sorting.

## Project Structure

The project structure is as follows:

imdb_project/
│
├── app/
│ ├── init.py
│ ├── auth.py
│ ├── upload.py
│ ├── view.py
│ ├── models.py
│ ├── static/
│ │ ├── styles.css
│ │ ├── script.js
│ ├── templates/
│ │ ├── login.html
│ │ ├── signup.html
│ │ ├── upload_progress.html
│ │ ├── dashboard.html
│
├── run.py
├── config.py
├── requirements.txt
├── Dockerfile
└── README.md


- `app/`: Directory containing Flask application code.
  - `__init__.py`: Initializes the Flask app and sets up routes.
  - `auth.py`: Contains routes for user authentication.
  - `upload.py`: Contains routes for uploading CSV files.
  - `view.py`: Contains routes for viewing movies data.
  - `models.py`: Defines database schema and indexes.
  - `static/`: Directory for static files (CSS, JavaScript).
  - `templates/`: Directory for HTML templates.
- `run.py`: Entry point for running the Flask application.
- `config.py`: Configuration file for Flask app.
- `requirements.txt`: List of Python dependencies.
- `Dockerfile`: Docker configuration file.
- `README.md`: This file.

## Running Instructions

1. Clone the repository:

git clone <repository_url>


2. Install dependencies:

pip install -r requirements.txt

3. Set up MongoDB:
   - Install MongoDB and start the MongoDB service.
   - Update the MongoDB URI in `config.py` if needed.

4. Run the Flask application:

python run.py

5. Access the application in your web browser at `http://localhost:5000`.

## Usage

- Register a new user or log in with existing credentials.
- Upload a CSV file containing movie data.
- View the uploaded movies data with pagination and sorting.

