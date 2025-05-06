# Start from a slim Python 3.10 image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install Node.js 18.x and npm
RUN apt-get update && \
    apt-get install -y curl gnupg && \
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy backend and frontend code
COPY backend /app/backend
COPY frontend /app/frontend


# Install frontend dependencies
WORKDIR /app/frontend/3000_project
RUN npm install


# Install Python dependencies
WORKDIR /app/backend
RUN pip install --no-cache-dir -r requirements.txt



# Expose ports: Flask (5000), Vite (5173)
EXPOSE 5123 5173


# Run Flask and React app concurrently
CMD ["sh", "-c", "cd /app/frontend/3000_project && npm run dev -- --host & cd /app/backend && python app.py"]
