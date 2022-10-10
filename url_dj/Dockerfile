FROM python:3.8.10-slim
# Necessary, so Docker doesn't buffer the output and that you can see the output 
# of your application (e.g., Django logs) in real-time.
ENV PYTHONUNBUFFERED 1
# Make a directory in your Docker image, which you can use to store your source code
RUN mkdir /url_dj
# Set the /django_recipe_api directory as the working directory
WORKDIR /url_dj
# Copies from your local machine's current directory to the django_recipe_api folder 
# in the Docker image
COPY . .
# Copy the requirements.txt file adjacent to the Dockerfile 
# to your Docker image
COPY ./req.txt /req.txt
# Install the requirements.txt file in Docker image
RUN pip install -r /req.txt
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

