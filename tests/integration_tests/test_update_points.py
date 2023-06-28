import pytest
import GUDLFT.server as server
from GUDLFT.server import app


class TestUpdatePoint:
    client = app.test_client()

    def test_update_point(self, monkeypatch, competitions_fixture, clubs_fixture):

        monkeypatch.setattr(server, "loadCompetitions", competitions_fixture)
        monkeypatch.setattr(server, "loadClubs", clubs_fixture)

        competitions = server.loadCompetitions
        clubs = server.loadClubs

        competition = competitions[1]
        club = clubs[1]

        club_point = int(club['points'])
        place_to_book = 3

        # On regarde les points du club dans le récap des points
        view_point_before = self.client.get('/viewsPoints')
        assert f"<td>{club['name']}</td><td>{club_point}</td>".replace(" ", "") \
               in view_point_before.data.decode().replace(' ', '').replace("\n", "")

        # On réserve 3 place et on contrôle que les 3 places sont bien soustraites
        result = self.client.post(
            '/purchasePlaces',
            data={
                "competition": competition["name"],
                "club": club["name"],
                "places": place_to_book
            }
        )
        assert f"Points available: {(club_point - place_to_book)}" in result.data.decode()

        # On regarde à nouveau la page récap des points pour contrôler que la maj est bien visible
        view_point_after = self.client.get('/viewsPoints')
        assert f"<td>{club['name']}</td><td>{(club_point - place_to_book)}</td>".replace(" ", "") \
               in view_point_after.data.decode().replace(' ', '').replace("\n", "")

