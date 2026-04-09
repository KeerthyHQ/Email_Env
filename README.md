# Email Support RL Environment

## Description
A reinforcement learning environment simulating customer support email handling.

## Features
- Multi-step email conversations
- Reward-based evaluation
- Easy, Medium, Hard tasks
- OpenEnv compatible

## Endpoints
- POST /reset
- POST /step

## Deployment
Hugging Face Space:
https://keerthybuilds-email-support-env.hf.space

## Why this environment?

Customer support automation is a real-world problem where AI agents must:
- understand user intent
- respond politely
- resolve issues effectively
- handle multi-step conversations

This environment simulates realistic email interactions and evaluates agent performance using structured rewards.

## Example

User: "I received a damaged product"

Good Response:
"Sorry for the issue. We will process your refund and arrange a return."

Bad Response:
"Ok noted"

screenshot 

<img width="781" height="607" alt="image" src="https://github.com/user-attachments/assets/8314675c-8fab-4f2f-a599-92f602d7747f" />
