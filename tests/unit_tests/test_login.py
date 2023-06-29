from GUDLFT.server import app
from GUDLFT.tests.conftest import client


class TestLoginLogout:
    client = app.test_client()

    def test_home(self):
        result = self.client.get("/")
        assert result.status_code == 200

    def test_login_valid(self):
        email = "john@simplylift.co"
        result = self.client.post('/showSummary', data={"email": email})
        assert result.status_code == 200

    def test_login_empty(self):
        email = ""
        result = self.client.post('/showSummary', data={"email": email})
        assert result.status_code == 200
        assert "email must not be empty" in result.data.decode()

    def test_login_invalid(self):
        email = "invalid@email.test"
        result = self.client.post('/showSummary', data={"email": email})
        assert result.status_code == 200
        assert "email not found" in result.data.decode()

    def test_view_points(self):
        result = self.client.get('/viewsPoints')
        assert result.status_code == 200

    def test_logout(self):
        result = self.client.get('/logout')
        assert result.status_code == 302
