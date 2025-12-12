# Stage 1: builder
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install --prefix=/install -r /app/requirements.txt
COPY . /app

# Stage 2: runtime
FROM python:3.11-slim
ENV TZ=UTC
WORKDIR /app

# Install system deps: cron, tzdata, git (git used by proof script)
RUN apt-get update && apt-get install -y --no-install-recommends \
    cron tzdata git && \
    rm -rf /var/lib/apt/lists/*

# Copy python packages from builder
COPY --from=builder /install /usr/local

# Copy app code
COPY . /app

# Setup cron file
RUN chmod 0644 /app/cron/2fa-cron && crontab /app/cron/2fa-cron

# Create volumes
RUN mkdir -p /data /cron
VOLUME ["/data", "/cron"]

# Expose port
EXPOSE 8080

# Start script
COPY start.sh /start.sh
RUN chmod +x /start.sh

CMD ["/start.sh"]
