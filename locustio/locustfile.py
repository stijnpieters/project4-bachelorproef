from locust import HttpLocust, TaskSet, task, between


class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("/login", {"username": "stijn", "password": "stijn"})

    def logout(self):
        self.client.post("/logout", {"username": "stijn", "password": "stijn"})

    @task(2)
    def index(self):
        self.client.get("/")

    @task(1)
    def cats(self):
        self.client.get("/cats")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(1, 3)
