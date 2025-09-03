#!/bin/bash
set -e

#clean dockert space
#docker system prune -a --volumes
docker container prune -f
docker image prune -f

# Import constants
source "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/constants.sh"

echo "Build and upload image to ACR name is: $ACR_NAME"

az acr login --name $ACR_NAME
docker build -t $FULL_IMAGE_NAME ../webapi
docker push $FULL_IMAGE_NAME

az containerapp update \
  --name $CONTAINER_APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --image $FULL_IMAGE_NAME \
  --cpu 1.0 --memory 2.0Gi 

