#!/bin/bash
# Redirect all output to log.txt
exec > log.txt 2>&1
echo "Starting setup script..."

# Run docker-compose with logging
docker-compose up --build --abort-on-container-exit

# After tests complete, explicitly stop the api container
docker stop api

echo "Setup script completed."
exit 0