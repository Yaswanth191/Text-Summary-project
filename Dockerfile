FROM python:3.8-slim-buster

# Install awscli and other dependencies in one layer, clean up afterwards
RUN apt-get update -y && \
    apt-get install -y awscli build-essential libzstd-dev python3-dev && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Upgrade pip, setuptools, and wheel
RUN pip install --upgrade pip setuptools wheel

# Install required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Optionally, install or upgrade specific packages
RUN pip install --upgrade accelerate
RUN pip install transformers accelerate

# Set the command to run the app
CMD ["python3", "app.py"]
