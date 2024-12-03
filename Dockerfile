# pull python image
FROM python:3.12.7-slim

# get dependencies for cv2 that is not part of base image
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0

# intall dependencies
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

# copy application code into directory
COPY . /app

# ensure port is exposed
EXPOSE 5000

# select flask app and run
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host", "0.0.0.0"]
