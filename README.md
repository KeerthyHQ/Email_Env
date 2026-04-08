# Email Support RL Environment

## Description
Simulates real-world customer support email interactions.

## Tasks
- Easy: basic polite response
- Medium: multi-step conversation
- Hard: full issue resolution

## Action Space
Agent sends a reply string.

## Observation Space
Email text + metadata.

## Reward
Keyword matching, politeness, resolution quality.

## Run

uvicorn server.app:app --reload  
python inference.py

## Docker

docker build -t email-env .  
docker run -p 8000:8000 email-env