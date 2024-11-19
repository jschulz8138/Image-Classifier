"""This module handles the happy and sad testing of the functionality of the system."""
import warnings
from result import result
from model_creation import model_creation

# Suppress specific warning
warnings.filterwarnings("ignore", category=DeprecationWarning)

IMAGE_TEST = "static/test_img/plane0.png"

def test_integration_valid_image_happy_path():
    """This test will correctly predict an image"""
    # Create the model
    client = app.test_client()
    client.testing = True
    model_creation()

    #Rest to save an image
    with open(IMAGE_TEST, "rb") as img_file:
        data = {
            "file": (img_file, "plane0.png")
        }
        response = client.post("/", data=data, content_type="multipart/form-data")

    # Test the response
    assert response.status_code == 200
    assert b"Result:" in response.data  # Verifying "Result:" is in the HTML response
    assert result() == "plane"

def test_integration_valid_image_sad_path():
    """This test will correctly predict an image"""
    # Create the model
    client = app.test_client()
    client.testing = True
    model_creation()

    #Rest to save an image
    with open("static/test_img/spy.png", "rb") as img_file:
        data = {
            "file": (img_file, "spy.png")
        }
        response = client.post("/", data=data, content_type="multipart/form-data")

    # Test the response
    assert response.status_code == 200
    assert b"Result:" in response.data  # Verifying "Result:" is in the HTML response
    assert result() != "spy"
