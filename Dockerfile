# ===== Stage 1: Builder =====
FROM node:20-slim AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install --only=production

COPY . .

# ===== Stage 2: Runtime =====
FROM node:20-slim

ENV NODE_ENV=production
ENV TZ=UTC

WORKDIR /app

# Install cron + timezone data
RUN apt-get update && \
    apt-get install -y cron tzdata && \
    ln -fs /usr/share/zoneinfo/UTC /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy built app
COPY --from=builder /app /app

# Create persistent dirs
RUN mkdir -p /data /cron && \
    chmod 755 /data /cron

# Install cron job
RUN chmod 644 /app/cron/2fa-cron && \
    crontab /app/cron/2fa-cron

# Volumes
VOLUME ["/data", "/cron"]

EXPOSE 8080

# Start cron and the Express server
CMD service cron start && node src/server.js