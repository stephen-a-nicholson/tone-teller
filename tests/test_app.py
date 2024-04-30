"""
Unit tests for the Tone Teller Flask application.

This module contains tests that verify the functionality of the Tone Teller web application,
ensuring that all routes behave as expected under various conditions. It tests the main
landing page for correct HTTP responses and content accuracy. These tests are crucial for
continual assurance of application stability and performance as updates and enhancements
are made to the application.

Dependencies:
    - unittest: Used for creating and running tests.
    - tone_teller.app: The Flask application to be tested.
"""

import unittest
from tone_teller.app import app


class TestApp(unittest.TestCase):
    """
    Define a suite of tests to confirm the correct behavior of the Flask application.
    """

    def setUp(self):
        """
        Prepare the test client before each test.

        This method sets up the application's test client, which will be used to make requests
        to the application's routes and assert their responses.
        """
        self.app = app.test_client()

    def test_index_route(self):
        """
        Test the index route of the web application to ensure it returns HTTP 200.

        This test checks that the main page is accessible and contains the correct content,
        verifying the presence of the expected byte string in the response data.
        """
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Tone Teller - Sentiment Analysis", response.data)


if __name__ == "__main__":
    unittest.main()
