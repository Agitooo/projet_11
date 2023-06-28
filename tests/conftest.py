import pytest
import os

from GUDLFT.server import app


@pytest.fixture
def client():
    server = app({"TESTING": True})
    with server.test_client() as client:
        yield client


@pytest.fixture
def clubs_fixture():
    return [
        {
            "name": "Simply Lift",
            "email": "john@simplylift.co",
            "points": "13"
        },
        {
            "name": "Iron Temple",
            "email": "admin@irontemple.com",
            "points": "4"
        },
        {
            "name": "She Lifts",
            "email": "kate@shelifts.co.uk",
            "points": "12"
         },
        {
            "name": "Best Club test",
            "email": "test@club.gg",
            "points": "45"
         }
    ]


@pytest.fixture
def competitions_fixture():
    return [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2024-10-22 13:30:00",
            "numberOfPlaces": "13"
        },
        {
            "name": "World Competition",
            "date": "2024-12-31 13:30:00",
            "numberOfPlaces": "99"
        }
    ]
