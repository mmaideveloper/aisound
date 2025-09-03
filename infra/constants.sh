#!/bin/bash

# Load environment variables from .env
set -a
source "$(cd "$(dirname "${BASH_SOURCE[0]}")/../webapi" && pwd)/.env"
set +a

DATA="$SECRET"
echo $DATA
az login --service-principal -u "5484c98d-4d67-47ca-ad11-db6add1f8bf2" -p "$DATA" --tenant "f3d3d42a-7c6d-4a44-aceb-ff9d7839f6d3"

az account set --subscription "5c0078f8-78f1-49be-9917-bdcc35f5e831" # Visual Studio Enterprise


# Constants
ACR_NAME="arcaisound"
RESOURCE_GROUP="rg-ai-sound"   
LOCATION="germanywestcentral"
CONTAINER_ENV="ai-sound-local"
CONTAINER_APP_NAME="api-ai-sound-local"

IMAGE_NAME="apiaisound"

IMAGE_TAG="$VERSION"


ACR_LOGIN_SERVER="${ACR_NAME}.azurecr.io"
FULL_IMAGE_NAME="${ACR_LOGIN_SERVER}/${IMAGE_NAME}:${IMAGE_TAG}"