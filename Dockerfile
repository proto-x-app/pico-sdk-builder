# Fetch ubuntu image
FROM ubuntu:23.10 AS builder

# Update, install necessary packages, and clean up in a single step to reduce layer size
RUN apt-get update && \
    apt-get install -y git cmake gcc-arm-none-eabi libstdc++-arm-none-eabi-newlib build-essential python3 python3-pip && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Pico SDK
RUN \
    mkdir -p /project/src/ && \
    cd /project/ && \
    git clone https://github.com/raspberrypi/pico-sdk.git --branch master && \
    cd pico-sdk/ && \
    git submodule update --init && \
    cd /
    
# Set the Pico SDK environment variable
ENV PICO_SDK_PATH=/project/pico-sdk/

# Copy in our source files
COPY src/* /project/src/

# Build project
RUN \
    mkdir -p /project/src/build && \
    cd /project/src/build && \
    cmake .. && \
    make
    
# Command that will be invoked when the container starts
ENTRYPOINT ["/bin/bash"]