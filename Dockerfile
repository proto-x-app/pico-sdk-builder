# Fetch ubuntu image
FROM ubuntu:23.10 AS builder

# Update, install necessary packages, and clean up in a single step to reduce layer size
RUN apt-get update && \
    apt-get install -y git cmake gcc-arm-none-eabi libstdc++-arm-none-eabi-newlib build-essential python3 python3-pip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Clone the pico-sdk repository and checkout a stable version
RUN git clone https://github.com/raspberrypi/pico-sdk.git \
    && cd pico-sdk \
    && git submodule update --init

# Set PICO_SDK_PATH environment variable
ENV PICO_SDK_PATH=/pico-sdk

# Clone the pico-examples repository
RUN git clone https://github.com/raspberrypi/pico-examples.git

# Set the working directory to the pico-examples folder
WORKDIR /pico-examples

# Run the build process
RUN mkdir build && cd build && cmake .. && make

## Build the final image    
# Use Python Alpine as the base image
FROM python:3.13.0a1-alpine3.18

# Create workspace, firmware, and examples directories
WORKDIR /workspace
RUN mkdir /workspace/firmware
RUN mkdir /workspace/examples

# Copy the build artifacts from the builder image
COPY --from=builder /pico-examples /pico-examples

# Copy app.py into the image
COPY app.py /workspace

# Entry point or CMD depending on your use-case
CMD ["python", "app.py"]

