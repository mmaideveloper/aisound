#!/bin/bash

# Import constants
source "$(dirname "$0")/constants.sh"

echo "Build and upload image to ACR name is: $ACR_NAME"

az acr login --name $ACR_NAME
docker build -t $FULL_IMAGE_NAME ../webapi
docker push $FULL_IMAGE_NAME

az containerapp update \
  --name $CONTAINER_APP_NAME \
  --resource-group $RESOURCE_GROUP \
  --image $FULL_IMAGE_NAME \
  --cpu 0.5 --memory 1.0Gi 

