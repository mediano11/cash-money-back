#
FROM python:3.11

#
WORKDIR /app

COPY requirements.txt ./

#
RUN pip install --no-cache-dir -r requirements.txt

#
COPY . .

# Set environment variables
ENV SERVER_METADATA_URL=https://accounts.google.com/.well-known/openid-configuration
ENV PYTHONPATH=/app/src/
