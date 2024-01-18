# Gradio Example
A Gradio Docker Example

## Introduction

This repository contains a simple example of using Gradio, a user-friendly library for creating customizable UI components for machine learning models. In this example, we'll show you how to quickly run a pre-built Gradio application using this Docker image.

## Prerequisite

Before you begin, make sure you have Docker installed on your system. You can download and install Docker from the [official website](https://www.docker.com/get-started).

## Usage

To run the Gradio example application using this Docker image, follow these steps:

Pull the [Docker image](https://hub.docker.com/repository/docker/pyouthful/gradio-example/tags?page=1&ordering=last_updated) from the Docker Hub repository:
```bash
docker pull pyouthful/gradio-example
```
> Alternatively, you can build an image from Dockerfile: `docker build -t="pyouthful/gradio-example" github.com/pyouthful/gradio-example`

Run the Docker container:
```bash
docker run -p 7860:7860 pyouthful/gradio-example
```
Once the container is running, you can access the Gradio application by opening a web browser and navigating to:

http://localhost:7860.

## Demo

This is a simple demo to show how it works on Huggingface:

https://huggingface.co/spaces/pyouthful/gradio-example



