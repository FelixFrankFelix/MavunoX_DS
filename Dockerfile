# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app



# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Set environment variables
ENV HOST=0.0.0.0
ENV PORT=80

# Command to run on container start
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
