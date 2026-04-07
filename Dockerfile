FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Render uses port 10000
EXPOSE 10000

# Start FastAPI backend
CMD ["uvicorn", "inference.app:app", "--host", "0.0.0.0", "--port", "10000"]