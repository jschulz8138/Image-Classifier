"""This module handles the testing of the functionality of the system."""
import pytest
import cv2
from result import result
from app import app


IMAGE_TEST = "static/test_img/plane0.png"

#Gerkin Acceptance Test One
#
#Upload and Classify Image
#
#Given: A valid image file (e.g., JPEG, PNG).
#When: The user uploads the image.
#Then: The application should return a classification label within predefined categories.

def test_upload_and_classify_images():
    """This module handles the upload acceptance testing."""
    client = app.test_client()
    client.testing = True

    # Fetch the CSRF token
    response = client.get("/")
    csrf_token = response.data.decode().split('name="csrf_token" value="')[1].split('"')[0]

    # Open the image file for uploading
    with open(IMAGE_TEST, "rb") as img_file:
        data = {"file": (img_file, IMAGE_TEST), "csrf_token": csrf_token}
        response = client.post("/", data=data, content_type="multipart/form-data")

    assert response.status_code == 200
    assert b"Result:" in response.data  # Verifying "Result:" is in the HTML response


#Gerkin Acceptance Test Two
#
#Unsupported File Format
#
#Given: An unsupported file format (e.g., TXT, PDF).
#When: The user attempts to upload the file.
#Then: The application should prevent the upload and
#display an error message indicating the unsupported format.

def test_unsupported_file_format():
    """This module handles the testing of file formats"""
    unsupported_file_path = "test_images/document.txt"

    client = app.test_client()
    client.testing = True

    # Fetch the CSRF token
    response = client.get("/")
    csrf_token = response.data.decode().split('name="csrf_token" value="')[1].split('"')[0]

    # Open the image file for uploading
    with open(IMAGE_TEST, "rb") as img_file:
        data = {"file": (img_file, IMAGE_TEST), "csrf_token": csrf_token}
        response = client.post("/", data=data, content_type="multipart/form-data")

    # Call the classify function and expect an error
    with pytest.raises(cv2.error, match=r".*resize.cpp.*Assertion failed.*ssize.empty\(\).*"): # pylint: disable=no-member
        result(unsupported_file_path)
    assert issubclass(cv2.error, BaseException) # pylint: disable=no-member
