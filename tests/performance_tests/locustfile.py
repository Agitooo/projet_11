from locust import HttpUser, task


class ProjectPerfTest(HttpUser):
    @task
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        email = "john@simplylift.co"
        self.client.post('/showSummary', {"email": email})

    @task
    def get_book_list(self):
        self.client.get("/book/Spring Festival/Simply Lift")

    @task
    def purchase_place(self):
        competition = "Spring Festival"
        club = "Simply Lift"
        places = "5"
        self.client.post('/purchasePlaces', {"competition": competition, "club": club, "places": places})

    @task
    def logout(self):
        self.client.get("/logout")
