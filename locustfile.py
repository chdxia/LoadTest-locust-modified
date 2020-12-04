from locust import HttpUser, TaskSet, task


class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def on_stop(self):
        self.logout()

    def login(self):
        self.client.post("/sessions", {"account": "admin", "password": "888888"})

    def logout(self):
        # self.client.delete("/sessions/1")
        pass

    @task(2)
    def warehouses(self):
        self.client.get("/warehouses")

    @task(1)
    def shifts(self):
        self.client.get("/shifts")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    min_wait = 5000
    max_wait = 9000
    host = 'http://localhost:8080/api/v1/app'
