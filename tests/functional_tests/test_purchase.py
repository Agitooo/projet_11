from server import app
from tests.conftest import client


class TestPurchase:
    client = app.test_client()

    def test_purchase_place_valid(self):
        competition = "Spring Festival"
        club = "Simply Lift"
        places = "5"
        result = self.client.post('/purchasePlaces', data={"competition": competition, "club": club, "places": places})
        assert result.status_code == 200
        assert "Great-booking complete!" in result.data

    def test_purchase_place_invalid_max_12(self):
        competition = "Spring Festival"
        club = "Simply Lift"
        places = "13"
        result = self.client.post('/purchasePlaces', data={"competition": competition, "club": club, "places": places})
        assert result.status_code == 200
        assert "You can only buy a maximum of 12 places." in result.data

    def test_purchase_place_invalid_not_enough(self):
        competition = "Spring Festival"
        club = "Simply Lift"
        places = "15"
        result = self.client.post('/purchasePlaces', data={"competition": competition, "club": club, "places": places})
        assert result.status_code == 200
        assert "Not enough points available." in result.data

    def test_purchase_place_invalid_club_or_competition(self):
        competition = "wrong competition"
        club = "wrong club"
        places = "2"
        result = self.client.post('/purchasePlaces', data={"competition": competition, "club": club, "places": places})
        assert result.status_code == 200
        assert "Something went wrong-please try again." in result.data
