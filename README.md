Of course, buddy! Here's the revised README in plain markdown format:

---

# `pico-sdk-builder`: Customizable Firmware Building Platform

## Table of Contents

1. [Introduction](#introduction)
2. [Custom Builds](#custom-builds)
3. [Setup and Installation](#setup-and-installation)
4. [Docker Integration](#docker-integration)
5. [Automated Deployment with GitHub Actions](#automated-deployment-with-github-actions)
6. [System Overview](#system-overview)
7. [Support and Feedback](#support-and-feedback)
8. [Acknowledgments](#acknowledgments)

## Introduction

`pico-sdk-builder` is a flexible firmware building platform designed to simplify and accelerate the development of firmware for the Pico microcontroller. It allows for customization of the SDK and application source, enabling a tailored firmware build process.

## Custom Builds

### Using Your Own SDK and Application

The building process is designed to be customizable, allowing you to specify your own SDK and application repositories. Set the build arguments `SDK_REPOSITORY` and `APP_REPOSITORY` to point to your repositories before building the Docker image.

### Docker Build Arguments

To customize the SDK and application repository during the Docker build, use the following arguments:

```
docker build --build-arg SDK_REPOSITORY=<your-sdk-repo-url> --build-arg APP_REPOSITORY=<your-app-repo-url> -t your-image-name .
```

Replace `<your-sdk-repo-url>` and `<your-app-repo-url>` with the URLs of your SDK and application repositories, respectively.

## Setup and Installation

Follow the standard installation steps, with the addition of the build arguments if you're using custom repositories.

### Pre-requisites

Ensure Docker is installed on your system.

### Steps

1. **Clone the repository** (if you haven't customized the Dockerfile):
```
git clone https://github.com/proto-x-app/pico-sdk-builder.git
```

2. **Build the Docker image with custom arguments** (optional):
```
docker build --build-arg SDK_REPOSITORY=<your-sdk-repo-url> --build-arg APP_REPOSITORY=<your-app-repo-url> -t pico-sdk-builder-image .
```

3. **Run the Docker container**:
```
docker run --rm -it -p 8000:8000 pico-sdk-builder-image
```

4. **Access the Web Interface**: Open your browser and navigate to `http://localhost:8000/`.

## Docker Integration

Detailed information about the Docker setup is provided, showcasing the multi-stage build process that ensures a clean, lightweight production image.

## Automated Deployment with GitHub Actions

The provided GitHub Actions workflow file `.github/workflows/deploy-new-version.yml` outlines the automated build and release process. Customize the `env` variables for `SDK_REPOSITORY` and `APP_REPOSITORY` to match your custom repositories.

## System Overview

The system uses a two-stage Docker build with the first stage for compiling the firmware and the second stage for serving it via a Flask web application.

## Support and Feedback

If you encounter any issues or have suggestions for improvements, please open an issue in the repository.

## Acknowledgments

Special thanks to those who contributed to the foundational technologies used in this platform.

---

Would you like to proceed with updating the README.md file with this content?