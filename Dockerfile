FROM python:3.9-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    golang \
    nmap \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose GUI port
EXPOSE 5000

# Default command
CMD ["python", "arsenal.py", "list-tools"]
