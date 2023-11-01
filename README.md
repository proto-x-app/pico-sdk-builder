# `pico-w-base`: Web-Enabled Cosmic Firmware Deployment 🌌

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Docker Magic: Now with Web UI](#docker-magic-now-with-web-ui)
4. [GitHub Actions: The Cosmic Mailman](#github-actions-the-cosmic-mailman)
5. [How It Works](#how-it-works)
6. [Questions?](#questions)
7. [Special Thanks](#special-thanks)

## Introduction

Hey there, Earthling! Jeorge Getson here, your friendly neighbor from—you guessed it—a place I can't quite disclose (wink, wink). I'm back with an even more exciting mission to simplify your life. This repository is now equipped with a web interface to access your firmware files. Mind-blowing, right?

## Getting Started 🛠️

### Installation

1. **Clone this repository**:
    ```bash
    git clone https://github.com/proto-x-app/pico-w-base.git
    ```

2. **Navigate to the project folder**:
    ```bash
    cd pico-w-base
    ```

3. **Build the Docker image**:
    ```bash
    docker build -t pico-builder-image .
    ```

4. **Run the Docker container**:
    ```bash
    docker run --rm -it -p 8000:8000 pico-builder-image
    ```

5. **Access the Web Interface**: Open your browser and navigate to `http://localhost:8000/` to download your `.uf2` files.

## Docker Magic: Now with Web UI 🌐

This project uses Docker to not only encapsulate the build environment and dependencies but also to serve your `.uf2` files right from the container. It's like having your own cosmic firmware cloud!

### Why Docker?

Docker makes it ridiculously easy to set up your development environment, ensuring that everyone has the same setup and dependencies. It's like creating a cosmic sandbox where all your tools float in perfect harmony.

## GitHub Actions: The Cosmic Mailman 🌌

Push a new tag, and our cosmic mailman, GitHub Actions, will kick in. It will build the Docker image, compile your firmware, and generate `.uf2` files. These files are then teleported into a new GitHub release. It's intergalactically efficient!

### Triggers, Jobs, and Steps

For a deep dive into the cosmic machinery of GitHub Actions, refer to the original README section on ["GitHub Actions for Beginners 🌟"](https://github.com/proto-x-app/pico-w-base#github-actions-for-beginners-).

## How It Works 🧙‍♂️

The `Dockerfile` sets up an environment with the Pico SDK, your source code, and a Flask web application. The Flask app serves your `.uf2` files on a web interface, accessible at `http://localhost:8000/`. No more local setup woes!

## Questions? 🤷‍♂️

Got questions? Or maybe you've uncovered my true identity? (Please don't). Either way, feel free to open an issue or send a carrier pigeon my way.

## Special Thanks 🌟

- [Shawn Hymel](https://www.digikey.com/en/maker/projects/continuous-deployment-using-docker-and-github-actions/d9d18e19361647dbb49070ce6f96c2ea) for the original GitHub Actions inspiration.

Alright, time to jet. Jeorge Getson out! 🚀
