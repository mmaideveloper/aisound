# aisound

##Description

Identify bee or predators per image and audio
Identify bee behavious/ sickness per image and audio
Able to upload new images and label them / autio for future training

##setup
conda env create -f environment.yml
conda activate aisounnd-env

##execute api
locally:   uvicorn webapi.server:app --reload



