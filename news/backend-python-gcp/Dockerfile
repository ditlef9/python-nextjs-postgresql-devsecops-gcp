# Specify Python
FROM python:latest

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Open port
EXPOSE 8080

# Add Python script
RUN mkdir /app
WORKDIR /app
COPY . .


# Install dependencies
RUN pip install -r requirements.txt

# Set Pythons path
ENV PYTHONPATH /app

# Run script
CMD [ "python", "main.py" ]
