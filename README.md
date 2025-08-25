# aisound

##Description

Identify bee or predators per image and audio
Identify bee behavious/ sickness per image and audio
Able to upload new images and label them / autio for future training

##setup
conda env create -f environment.yml
conda activate aisound-env

##execute api

locally from parent:
uvicorn webapi.server:app --reload

localy from webpi:
uvicorn server:app --reload

docker:

docker build -t aisound-api .
docker run -d -p 8000:8080 aisound-api

docker ps -a  
docker logs <containerid>

docker remote all intances:
docker rm -f $(docker ps -aq)

docker remove all imanges:

docker rmi -f $(docker images -aq)

---


#Install to Azure Container App







