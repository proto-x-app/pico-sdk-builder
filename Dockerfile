# Use an official Ubuntu as a builder image
FROM ubuntu:23.10 AS builder

# Set environment variables for SDK and APP repository
ARG SDK_REPOSITORY=https://github.com/proto-x-app/pico-sdk.git
ARG APP_REPOSITORY=https://github.com/proto-x-app/pico-app-template.git

# Install necessary packages in a single RUN command to reduce image size
RUN apt-get update \
    && apt-get install -y \
        git \
        cmake \
        gcc-arm-none-eabi \
        libstdc++-arm-none-eabi-newlib \
        build-essential \
        python3 \
        python3-pip \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Clone, build, and install the pico-sdk
WORKDIR /pico-sdk
RUN git clone $SDK_REPOSITORY . \
    && git submodule update --init

# Set PICO_SDK_PATH environment variable
ENV PICO_SDK_PATH=/pico-sdk

# Clone and build the pico-app
WORKDIR /pico-app
RUN git clone $APP_REPOSITORY . \
    && mkdir build \
    && cd build \
    && cmake .. \
    && make

# Copy Flask app to /app directory
COPY app/ /app/

# Move the build artifacts to a common workspace
RUN mkdir -p /workspace/source \
    && mkdir -p /workspace/firmware \
    && mkdir -p /workspace/html \ 
    && mkdir -p /workspace/static 

WORKDIR /workspace
RUN python3 /app/restructure.py

# Use an official Python runtime as a parent image
FROM python:3.13.0a1-alpine3.18

# Create a non-root user and switch to it
ARG USERNAME=JoergeGetson
RUN adduser -D $USERNAME

# Set the working directory and copy build artifacts
WORKDIR /workspace
COPY --from=builder --chown=$USERNAME:$USERNAME /workspace/source /workspace/source
COPY --from=builder --chown=$USERNAME:$USERNAME /workspace/firmware /workspace/firmware
COPY --from=builder --chown=$USERNAME:$USERNAME /workspace/static /workspace/static

WORKDIR /app
COPY --chown=$USERNAME:$USERNAME app/ /app/
COPY --from=builder --chown=$USERNAME:$USERNAME /workspace/html /app/html
COPY --from=builder --chown=$USERNAME:$USERNAME /workspace/static /app/static

# Copy Flask app to /app directory

# Switch to non-root user
USER $USERNAME

# Switch back to root to install dependencies
USER root
RUN pip install --no-cache-dir -r requirements.txt \
    && pip install gunicorn==21.2.0

# Switch back to non-root user for better security
USER $USERNAME

# Declare volumes and expose ports
VOLUME ["/workspace/firmware"]
VOLUME ["/workspace/source"]
EXPOSE 8000

# Run gunicorn to serve the Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]
