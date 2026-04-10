# 🌍 AI Pollution Control OpenEnv

## Overview

AI agent simulation for pollution control using a reinforcement learning environment.

## Features

- OpenEnv-compatible API
- Reset + Step endpoints
- Pollution control simulation
- Gradio UI for demo

## Run

docker build -t pollution-env .
docker run -p 7860:7860 pollution-env

## API

- POST /reset
- POST /step
