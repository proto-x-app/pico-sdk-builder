# `pico-builder`: Web-Enabled Firmware Deployment

## Table of Contents

1. [Introduction](#introduction)
2. [Setup and Installation](#setup-and-installation)
3. [Docker Integration](#docker-integration)
4. [Automated Deployment with GitHub Actions](#automated-deployment-with-github-actions)
5. [System Overview](#system-overview)
6. [Support and Feedback](#support-and-feedback)
7. [Acknowledgments](#acknowledgments)

## Introduction

Welcome to the `pico-builder` project, a robust solution for web-enabled firmware deployment. This platform provides an intuitive web interface to seamlessly access and deploy your firmware files.

## Setup and Installation

### Pre-requisites

Ensure you have Docker installed on your system.

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/proto-x-app/pico-builder.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd pico-builder
    ```

3. **Build the Docker image**:
    ```bash
    docker build -t pico-builder-image .
    ```

4. **Start the Docker container**:
    ```bash
    docker run --rm -it -p 8000:8000 pico-builder-image
    ```

5. **Access the Web Interface**: Launch your browser and head to `http://localhost:8000/` to retrieve your `.uf2` files.

## Docker Integration

This project harnesses Docker to encapsulate the build environment and its dependencies. Additionally, it serves the `.uf2` files directly from the container. Docker ensures a consistent development environment for all users.

### Why Docker?

Docker streamlines the development environment setup, ensuring consistency across different setups. It provides an isolated environment where all required tools and dependencies coexist without conflicts.

## Automated Deployment with GitHub Actions

Leverage the power of GitHub Actions to automate your deployment. Upon pushing a new tag, GitHub Actions initiates a process to build the Docker image, compile the firmware, and subsequently generate `.uf2` files. These files are then automatically attached to a new GitHub release.

### Configuration Details

For an in-depth understanding of the GitHub Actions setup and its intricacies, refer to the detailed section on ["GitHub Actions Configuration"](https://github.com/proto-x-app/pico-builder#github-actions-configuration).

## System Overview

The provided `Dockerfile` configures an environment with the Pico SDK, your source files, and a Flask web application. This Flask application facilitates the web-based interface, available at `http://localhost:8000/`, to access the `.uf2` files.

## Support and Feedback

Encountered an issue or have suggestions for improvement? Open an issue in the repository, and we'll address it promptly.

## Acknowledgments

- Special thanks to [Shawn Hymel](https://www.digikey.com/en/maker/projects/continuous-deployment-using-docker-and-github-actions/d9d18e19361647dbb49070ce6f96c2ea) for the foundational insights on GitHub Actions.

Thank you for choosing `pico-builder`. Happy deploying!
