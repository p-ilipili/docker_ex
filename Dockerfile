FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Upgrade pip3 to the latest version
#RUN pip3 install --upgrade pip

# Install requests using pip3
RUN pip3 install --no-cache-dir requests
# Define volumes for logs and scripts
VOLUME ["/app", "/api_log"]