# French Pronunciation Agent

<!-- Badges (adjust or remove as needed) -->
![Status](https://img.shields.io/badge/status-active-success)
![License](https://img.shields.io/badge/license-MIT-informational)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/backend-Flask-lightgrey)
![Frontend](https://img.shields.io/badge/frontend-HTML%2FCSS-lightgrey)

---

## TL;DR
A simple web application to help users practice French pronunciation: record your voice, compare it against a reference phrase, get quick feedback, and iterate.

**Live demo:** https://extraordinary-sopapillas-ea8bbe.netlify.app/  <!-- Update if needed -->

---

## Table of Contents
- [Overview](#overview)
- [Demo](#demo)
- [Features](#features)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Requirements](#requirements)
- [Quickstart](#quickstart)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Configuration](#configuration)
- [Testing](#testing)
- [Deployment](#deployment)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

---

## Overview
This project provides a minimal, beginner-friendly **French pronunciation trainer**:
- Records speech in the browser.
- Sends audio to a lightweight Flask API for recognition/analysis.
- Offers immediate feedback so learners can adjust their pronunciation.

It is **portable** (static frontend + small Python backend) and **deployable** on common services (Render/Netlify).

---

## Demo
- **Frontend (static):** Open `index.html` or the **live demo** linked above.
- **Backend (Flask API):** Run locally with `python app.py` (see [Quickstart](#quickstart)).

> Tip: Use the included `test_audio.wav` or `test_audio.mp3` to verify the end-to-end flow.

---

## Features
- ✅ Record & play back audio in the browser.
- ✅ Compare recorded speech to a reference sentence.
- ✅ Display quick feedback (recognition text vs input).
- ✅ Clean, responsive UI.
- ✅ Ready to deploy (Render + Netlify).

---

## Architecture
```
Browser (Mic, MediaRecorder, UI) ──▶ Flask API (SpeechRecognition/gTTS) ──▶ Feedback (text/audio)
              ▲                                     │
              └─────────────── Fetch/AJAX ──────────┘
```
- **Frontend:** `index.html`, `styles.css` (+ optional JS section inline).
- **Backend:** `app.py` exposes endpoints to receive audio and return recognition/feedback.
- **Artifacts:** `test_audio.wav`, `test_audio.mp3` for quick testing.

---

## Tech Stack
- **Frontend:** HTML, CSS (vanilla)
- **Backend:** Python, Flask
- **Speech:** `SpeechRecognition`, optional `gTTS`
- **Infra:** Render (backend), Netlify (frontend)

---

## Requirements
- Python 3.10+
- `pip install -r requirements.txt`

Typical packages (from `requirements.txt`):
```
Flask
SpeechRecognition
gTTS
werkzeug
```
> Adjust this list to match your exact `requirements.txt`.

---

## Quickstart
1. **Clone** the repo:
   ```bash
   git clone https://github.com/jkbarrerab/french-pronunciation-agent.git
   cd french-pronunciation-agent
   ```

2. **Install** dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run** the backend:
   ```bash
   python app.py
   ```
   Backend runs at `http://127.0.0.1:5000/` by default.

4. **Open** the frontend:
   - Double‑click `index.html` to open in your browser, or
   - Serve it with any static server and point it to your backend URL.

---

## Usage
1. Type or paste a **reference sentence** in French.
2. Click **Record**, speak the phrase, then **Stop**.
3. The app will transcribe and compare your audio.
4. Review the feedback; repeat and improve.

> Tip: Use earphones and a quiet room for cleaner recordings.

---

## Project Structure
```
.
├── app.py                 # Flask API (audio receive, analysis, response)
├── index.html             # Main UI
├── styles.css             # Styling
├── requirements.txt       # Python dependencies
├── render.yaml            # Render deployment config (backend)
├── render-build.sh        # Optional install script for Render
├── test_audio.wav         # Sample input
├── test_audio.mp3         # Sample input
└── README.md              # This file
```
> If you add JS as a separate file (e.g., `script.js`), list it here as well.

---

## API Reference
> **Note:** Adjust paths to match `app.py` if they differ.

### `POST /api/analyze`
Accepts audio (e.g., `multipart/form-data` or `audio/wav`) and a reference text.
- **Body:**
  - `audio`: recorded audio blob
  - `text`: reference sentence to compare
- **Response (JSON):**
  - `transcript`: recognized text
  - `match_score` (optional): simple similarity metric
  - `notes`: extra feedback

### `GET /health`
Simple health check, returns `{{"status": "ok"}}`.

---

## Configuration
Common environment variables (if used):
```
FLASK_ENV=development
PORT=5000
```
You can also configure a **proxy/base URL** for the frontend to call the backend (e.g., `REACT_APP_API_URL` if using a build system). For raw HTML, keep the API URL in a `<script>` block or a small config file.

---

## Testing
- **Manual:** Use the test audio files to validate the pipeline.
- **Automated (optional):** Add `pytest` for unit tests on utility functions (e.g., text similarity, audio handling).

Example placeholder test structure:
```
tests/
  ├── test_similarity.py
  └── conftest.py
```

---

## Deployment

### Backend (Render)
1. Create a **New Web Service** on Render and link this repo.
2. **Build Command:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Start Command:**
   ```bash
   python app.py
   ```
4. After deploy, note the backend URL (e.g., `https://your-service.onrender.com`).

### Frontend (Netlify)
1. Drag‑and‑drop `index.html` (and assets) into Netlify or connect this repo’s `main` branch.
2. Ensure the JavaScript points to your **Render backend** URL.

---

## Roadmap
- [ ] Better UI/UX (loading states, waveforms)
- [ ] Real‑time feedback (phoneme‑level hints)
- [ ] Progress tracking per user
- [ ] Model‑based scoring (e.g., small ASR/phoneme models)

---

## Contributing
1. Fork the repo
2. Create a branch: `git checkout -b feature/my-change`
3. Commit: `git commit -m "feat: add X"`
4. Push: `git push origin feature/my-change`
5. Open a Pull Request

---

## License
MIT — see `LICENSE` (or add one if missing).

---

## Acknowledgements
- Built with Flask + vanilla HTML/CSS.
- Inspired by simple pronunciation training workflows.

---

## Contact
Created by **Jorge Karolt Barrera Ballesteros** — feel free to reach out on LinkedIn or open an issue.
