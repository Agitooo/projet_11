from GUDLFT.server import app


class TestBook:
    client = app.test_client()

    def test_book_competition_valid(self):
        result = self.client.get("/book/Spring Festival/Simply Lift")
        assert result.status_code == 200

    def test_book_competition_invalid(self):
        result = self.client.get("/book/wrong competition/wrong club")
        assert "Something went wrong-please try again" in result.data.decode()

    # All competition are done...
    def test_book_competition_done(self):
        result = self.client.get("/book/Spring Festival/Simply Lift")
        assert result.status_code == 200
        assert "This competition is done" in result.data.decode()

