# Retrieve official Python 2.7 image from public Docker Hub repository.
FROM python:2.7

# Open port 9000 for container.
EXPOSE 9000

# Create a new directory to store the API server.
RUN mkdir /app

# Add required files inside the new directory.
ADD . /app

# Set the working environment to the to created directory.
WORKDIR /app

# Install the Python module dependencies.
RUN pip install -r requirements.txt

# Setup the environment variables.
ENV MAILGUN_API_KEY=abc1234
ENV MAILGUN_DOMAIN_NAME="sandboxtest.com"
ENV MANDRILL_API_KEY=abc1234

# Run unit tests.
RUN python tests.py

# Launch the API server.
CMD ["python", "server.py", "9000"]
