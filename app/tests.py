import unittest
from app import app, mongo

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        # Set up Flask app for testing
        app.config['TESTING'] = True
        app.config['MONGO_URI'] = 'mongodb://localhost:27017/imdb'  # Use a test database
        self.app = app.test_client()

    def tearDown(self):
        # Clean up after each test
        with app.app_context():
            mongo.db.drop_collection('movies')
            mongo.db.drop_collection('users')

    def test_index_route(self):
        # Test the index route
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sign Up', response.data)

    def test_signup_route(self):
        # Test the signup route
        response = self.app.post('/signup', data={'email': 'test@example.com', 'password': 'password', 'confirm_password': 'password'})
        self.assertEqual(response.status_code, 302)  # Should redirect to login page

    def test_login_route(self):
        # Test the login route
        response = self.app.post('/login', data={'email': 'test@example.com', 'password': 'password'})
        self.assertEqual(response.status_code, 302)  # Should redirect to dashboard

    def test_movies_route(self):
        # Test the movies route
        response = self.app.get('/movies')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Movies/Shows', response.data)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
