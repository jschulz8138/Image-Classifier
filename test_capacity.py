"""
This module handles a capacity test for predicting images
"""
from __future__ import annotations

from locust import HttpUser, task, between
#from app import app

PROCESS = None

IMAGE_TEST = "static/test_img/plane0.png"

class WebsiteUser(HttpUser):
    """This test class handles simulates one user"""
    wait_time = between(2, 5)
    @task
    def load_main(self):
        """This function handles getting the index page"""
        response = self.client.get("/")
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

    @task
    def predict_image_file(self):
        """This function handles uploading an image"""
        # send a POST request to the prediction route with the test image file
        response = self.client.get("/")
        csrf_token = (
            response.text.split('name="csrf_token" value="')[1].split('"')[0])

        with open(IMAGE_TEST, "rb") as img_file:
            data = {
                "csrf_token": csrf_token
            }
            files = {
                "file": ("plane0.png", img_file, "image/png")
            }
            response = self.client.post("/", data=data, files=files)
        assert response.status_code == 200, f"Expected 200 but got {response.status_code}"

        assert "Result:" in response.text  # Verifying "Result:" is in the HTML response
