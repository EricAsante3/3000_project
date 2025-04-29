# Start from a slim Python 3.10 image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy backend and frontend code
COPY . /app/backend

# Install Python dependencies
WORKDIR /app/backend
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports: Flask (5000), Vite (5173)
EXPOSE 5123

# Run Flask and React app concurrently
CMD ["sh", "-c", "cd /app/backend && python app.py"]
