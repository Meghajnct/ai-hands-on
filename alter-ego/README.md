---
title: "Alter Ego AI"
emoji: "🧠"
colorFrom: "purple"
colorTo: "indigo"
sdk: gradio
sdk_version: "5.0.0"
python_version: "3.11"
app_file: app.py
pinned: false
---

# Alter Ego AI

An AI-powered digital twin that represents Megha Gupta in a conversational, professional web experience.

## Overview

This project turns a static personal profile into an interactive career assistant. Visitors can ask questions about:

- background and experience
- technical skills and strengths
- project approach and expertise
- career journey and professional focus
- how to get in touch

The app uses a Gradio chat interface and OpenAI chat completions to answer questions grounded in the user's profile summary and LinkedIn profile context.

## Features

- Conversational digital twin experience
- Professional profile-based responses
- Lead capture for interested visitors
- Structured follow-up logging for unanswered questions
- Clean, branded UI for a personal portfolio or professional website

## Stack

- Python
- Gradio
- OpenAI API
- PyPDF
- python-dotenv

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

## Project files

- `app.py` — Gradio chat interface and model orchestration
- `context.py` — system prompt and profile context
- `tools.py` — tool calling and lead/question logging
- `styles.py` — custom UI styling
- `summary.txt` — profile summary used by the AI
- `Profile.pdf` — source profile content for context extraction

## Use case

This is ideal for a personal brand, portfolio, recruiter funnel, or AI-powered professional landing page that can answer common questions automatically while still feeling personal and human.
