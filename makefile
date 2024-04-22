# Variables
IMAGE_NAME = air-quality-dashboard

# Commands
.PHONY: help build run clean

help:
	@echo "Available commands:"
	@echo "  make build   - Build the Docker image"
	@echo "  make run     - Run the Docker container"
	@echo "  make clean   - Remove Docker image and cleanup"

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run -p 8501:8501 $(IMAGE_NAME)

clean:
	docker rmi $(IMAGE_NAME)
