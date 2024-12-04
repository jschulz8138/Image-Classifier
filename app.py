"""Image Classification application trained on a CNN model that can be accessed from a browser"""
import os
from flask import Flask, render_template, request, abort
import numpy as np
import cv2 as cv
from keras import models
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config["SECRET_KEY"] = "this-is-a-secret-key"
csrf = CSRFProtect()
csrf.init_app(app)
app.debug = False

# Load the pre-trained model
model = models.load_model("image_classifier.h5")

# Class names for CIFAR-10
class_names = [
    "plane",
    "car",
    "bird",
    "cat",
    "deer",
    "dog",
    "frog",
    "horse",
    "ship",
    "truck",
]


def preprocess_image(img_path):
    """Adjusts the image to a standard format so that it can be read by the model"""
    img = cv.imread(img_path) # pylint: disable=no-member
    img = cv.resize(img, (32, 32)) # pylint: disable=no-member
    img = img / 255.0
    img = img[None, :]
    return img


@app.route("/", methods=["GET", "POST"])
def index():
    """RESTful application that serves as a GUI for a user to check images to the trained model"""
    if request.method not in ["GET", "POST"]:
        abort(405)  # 405 Method Not Allowed
    if request.method == "POST":
        # Handle the uploaded image
        file = request.files["file"]
        if file:
            # Save the uploaded image
            if not os.path.exists("static/uploads"):
                os.makedirs("static/uploads")
            img_path = "static/uploads/uploaded_image.png"
            file.save(img_path)
            # Preprocess the image
            img = preprocess_image(img_path)
            # Make a prediction
            prediction = model.predict(img)
            result = class_names[np.argmax(prediction)]
            return render_template("index.html", result=result, image_path=img_path)
    return render_template("index.html", result=None, image_path=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
