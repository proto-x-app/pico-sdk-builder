# `pico-w-blink`: The Cosmic Blinker 🌌

## Table of Contents

1. [Introduction](#introduction)
2. [Getting Started](#getting-started)
3. [Docker Magic](#docker-magic)
4. [GitHub Actions: The Space Elevator](#github-actions-the-space-elevator)
5. [Git Flow for Earthlings, by Joerge Getson](docs/using_git.md)
6. [Further Reading](#further-reading)


Hey there, Earthling! Jeorge Getson here, your friendly neighbor from—you guessed it—a place I can't quite disclose (wink, wink). But let's just say it's far, far away and I'm here on a secret mission to simplify your life.

Ever wondered how to make a Raspberry Pi Pico blink like a disco ball at an intergalactic party? Well, you've landed on the right repo! 

## What's This All About? 🤔

This repository is a starter kit for anyone looking to build firmware for the Raspberry Pi Pico. We're using Docker to compile our firmware, GitHub Actions for the deployment, and some good ol' C code for the blinky magic.

## Installation 🛠️

1. **Clone this repository**: Yup, just like how we... never mind. Just run this command:
    ```bash
    git clone https://github.com/proto-x-app/pico-w-blink.git
    ```

2. **Navigate to the project folder**:
    ```bash
    cd pico-w-blink
    ```

3. **Build the Docker image**:
    ```bash
    docker build -t pico-builder-image .
    ```

4. **Create a Docker container**:
    ```bash
    docker create --name pico-builder-container pico-builder-image
    ```

5. **Retrieve the `.uf2` file**:
    ```bash
    docker cp pico-builder-container:/project/src/build/pico-w-blink.uf2 ./pico-w-blink.uf2
    ```

## GitHub Actions 🚀

Whenever you push a new tag, our GitHub Actions workflow will kick in. It'll build the Docker image, compile the firmware, and generate a `.uf2` file. Then, like a cosmic mailman, it'll deliver this file right to the GitHub releases.

### GitHub Actions for Beginners 🌟

Alright, listen up, cadets! GitHub Actions is like your robotic butler. It automates all sorts of GitHub tasks: testing, deploying, you name it. The way it works is pretty nifty. Let me break it down for you:

#### 1. Triggers 🎬

First off, you need something to set the whole machine in motion. In our case, it's pushing a new tag to the repo. This is like ringing the butler's bell; it wakes up GitHub Actions and says, "Hey, we've got work to do!"

#### 2. Workflow File 📜

When the bell rings, GitHub Actions looks for a set of instructions, which you'll find in the `.github/workflows/` directory. It's like a recipe for your butler, telling him exactly what to do step-by-step. We've named ours something pretty straightforward: `deploy-new-version.yml`.

#### 3. Jobs 👷‍♂️

Inside this workflow file, you'll find something called 'jobs'. No, not Steve Jobs, just jobs. These are individual tasks that your butler will carry out. Think of them as chores on a to-do list.

#### 4. Steps 👟

Each job has a series of 'steps', which are the nitty-gritty details. This is where you tell your butler, "First, do this. Then, do that." For example, 'Check out this repository' or 'Build Docker image'.

#### 5. Run Command 🏃‍♂️

In some steps, you'll see a `run` command. This is where you get to boss GitHub Actions around by giving it some shell commands to execute. It's like saying, "Jeeves, fetch my pipe and slippers!"

#### 6. Environment Variables 🌍

Sometimes, you'll need to pass along some extra info. This is where 'env' (short for 'environment variables') comes in. It's like whispering a secret code to your butler that he'll need later on.

#### 7. Release 🎉

At the end of it all, if everything goes smoothly, your butler—ahem, GitHub Actions—will take the freshly baked `.uf2` file and neatly place it in GitHub releases. It's like having your cake and eating it too, but without lifting a finger.

And there you have it! You've just automated your whole build and deploy process without breaking a sweat. GeorgeJetsome would be proud! 🚀

## How It Works 🧙‍♂️

The magic potion is in the `Dockerfile`. This file sets up an environment with all the right ingredients for the Pico SDK and your project's source code. It then compiles the firmware so that you don't have to bother with any local setup. Convenient, huh?

## Questions? 🤷‍♂️

Got questions? Or maybe you've uncovered my true identity? (Please don't). Either way, feel free to open an issue or send a carrier pigeon my way.

Alright, time to jet. Jeorge Getson out! 🚀

## Special thanks

* Shawn Hymel and his wonderful article on getting the toolchain and action workflow up and running. [continuous-deployment-using-docker-and-github-actions](https://www.digikey.com/en/maker/projects/continuous-deployment-using-docker-and-github-actions/d9d18e19361647dbb49070ce6f96c2ea)
