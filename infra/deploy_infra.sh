#!/bin/bash

# Import constants
source "$(dirname "$0")/constants.sh"

echo "Using Resource Group: $RESOURCE_GROUP to deploy the resources"

az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file main.bicep \
  --parameters \
  acrName=$ACR_NAME \
  containerEnv=$CONTAINER_ENV \
  containerAppName=$CONTAINER_APP_NAME\
  location=$LOCATION\
  imageName=$FULL_IMAGE_NAME\

