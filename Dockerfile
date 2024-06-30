# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONPATH=/app/src

# Set the working directory inside the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container
COPY . .


# Expose the port that FastAPI runs on
EXPOSE 3000

# Command to run your FastAPI application using uvicorn
# CMD echo "Running setup tasks..." \
#     && prisma generate \
#     && uvicorn src.main:app --host 0.0.0.0 --port 3000
CMD ["sh", "-c", "echo 'Running setup on port: $PORT' && prisma generate && uvicorn src.main:app --host 0.0.0.0 --port 3000"]
