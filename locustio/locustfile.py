from locust import HttpLocust, TaskSet, task, between
from locust.contrib.fasthttp import FastHttpLocust

counter = 0


class UserBehavior(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        global counter
        self.client.post("/registration", {"username": "user" + str(counter), "password": "password"})
        self.client.post("/login", {"username": "user" + str(counter), "password": "password"})
        counter += 1

    def logout(self):
        self.client.get("/logout")

    # The number between brackets means the weight of the task
    @task(1)
    def index(self):
        self.client.get("/")

    @task(1)
    def dogs(self):
        self.client.get("/dogs")


class WebsiteUser(FastHttpLocust):
    task_set = UserBehavior
    wait_time = between(3, 5)
