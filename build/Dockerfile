# Use official Python & Alpine as the parent image
FROM python:3.7.4-alpine3.10

# Set the working directory to /app
WORKDIR /app

# Copy app.py into the container at /app
COPY app.py requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make ports available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME apitest

# Always run python when the container launches
ENTRYPOINT ["python"]

# Start app.py by default if no other commands are given at launch
CMD ["app.py"]