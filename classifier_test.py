"""This module handles the testing of the functionality of the system."""
import warnings
from result import result
from model_creation import model_creation
from app import preprocess_image, app

# Suppress specific warning
warnings.filterwarnings("ignore", category=DeprecationWarning)

IMAGE_TEST = "static/test_img/plane0.png"

def test_preprocess_image_height():
    """This test case handles loading an image, checking if the new height is equal"""
    assert preprocess_image(IMAGE_TEST).shape[1] == 32

def test_preprocess_image_width():
    """loads an image.Checks if the new width is equal to the expected value."""
    assert preprocess_image(IMAGE_TEST).shape[2] == 32

def test_preprocess_image_return_type():
    """This test case handles loading an image and checking the return type."""
    assert preprocess_image(IMAGE_TEST) is not None

def test_result_return_type():
    """This test case handles entire functionality of result and checks the return type"""
    assert result(IMAGE_TEST) is not None

def test_dynamic_result_test():
    """This test case is a dynamic test
    testing two of each image to ensure the model is trained and predicting correctly"""
    class_names = ["plane", "car", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    image_path_dict = {
        IMAGE_TEST : class_names[0],
        "static/test_img/car0.png" : class_names[1],
        "static/test_img/car1.png" : class_names[1],
        "static/test_img/bird0.png" : class_names[2],
        "static/test_img/bird1.png" : class_names[2],
        "static/test_img/cat0.png" : class_names[3],
        "static/test_img/cat1.png" : class_names[3],
        "static/test_img/deer0.png" : class_names[4],
        "static/test_img/deer1.png" : class_names[4],
        "static/test_img/dog0.png" : class_names[5],
        "static/test_img/dog1.png" : class_names[5],
        "static/test_img/frog0.png" : class_names[6],
        "static/test_img/frog1.png" : class_names[6],
        "static/test_img/horse0.png" : class_names[7],
        "static/test_img/horse1.png" : class_names[7],
        "static/test_img/ship0.png" : class_names[8],
        "static/test_img/truck0.png" : class_names[9],
        "static/test_img/truck1.png" : class_names[9]
    }
    for key, _value in image_path_dict.items():
        assert isinstance(result(key), str)


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
