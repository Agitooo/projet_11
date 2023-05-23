import pytest
import os
# import server

from GUDLFT.server import app
# from flask import Flask


@pytest.fixture
def client():
    server = app({"TESTING": True})
    with server.test_client() as client:
        yield client


# from server import app
#
#
# @pytest.fixture(scope='module')
# def test_client():
#     # Set the Testing configuration prior to creating the Flask application
#     os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
#     flask_app = app()
#
#     # Create a test client using the Flask application configured for testing
#     with flask_app.test_client() as testing_client:
#         # Establish an application context
#         with flask_app.app_context():
#             yield testing_client  # this is where the testing happens!

