<div align="center">

# faceauth-linux

Local face authentication prototype for Linux using facial landmarks, liveness checks and future PAM-ready verification.

![Status](https://img.shields.io/badge/status-early%20prototype-orange)
![Platform](https://img.shields.io/badge/platform-Linux-blue)
![Primary target](https://img.shields.io/badge/primary%20target-Fedora-purple)
![Language](https://img.shields.io/badge/language-Python-yellow)
![Security](https://img.shields.io/badge/security-password%20fallback%20required-red)

</div>

> This project is experimental. It is not intended to replace passwords completely.

---

## Overview

`faceauth-linux` explores local face-based authentication for Linux systems.

The initial target is Fedora Linux, but the project is designed to remain generic enough for other Linux distributions.

The project is being developed incrementally, starting with camera access and facial landmarks before moving into liveness checks, face verification and optional PAM integration.

---

## Current status

| Area | Status |
|---|---|
| Project scaffold | Done |
| Python virtual environment | Done |
| Camera access probe | Done |
| MediaPipe Face Landmarker | Done |
| Facial landmarks | Done |
| Blendshapes | Done |
| Head pose detection | Pending |
| Liveness challenge | Pending |
| Face enrollment | Pending |
| Face verification | Pending |
| PAM integration | Pending |

Current milestone:

**v0.1 - Camera and landmarks**

---

## Current capabilities

Implemented:

- [x] Initial project scaffold
- [x] Python virtual environment setup
- [x] Camera access probe
- [x] MediaPipe Face Landmarker prototype
- [x] Basic facial landmark extraction
- [x] Blendshape output enabled

Pending:

- [ ] Basic head pose detection
- [ ] Liveness challenge prototype
- [ ] Face enrollment
- [ ] Face verification
- [ ] PAM proof of concept
- [ ] Fedora integration notes

---

## Project goals

The main goal is to build a local authentication prototype that combines:

- facial landmark detection;
- basic liveness validation;
- face verification;
- Linux-friendly CLI tooling;
- future PAM integration;
- Fedora-first documentation.

The project should remain:

- local-first;
- auditable;
- easy to test;
- safe to disable;
- password-fallback friendly.

---

## Non-goals

This project does not currently aim to defeat:

- advanced video replay attacks;
- deepfake attacks;
- compromised host environments;
- professional biometric spoofing;
- hardware-level attacks.

A normal password fallback must always remain available.

---

## Architecture draft

```text
Camera
  ↓
Frame capture
  ↓
Face landmark detection
  ↓
Head pose / expression analysis
  ↓
Liveness challenge
  ↓
Face verification
  ↓
CLI result
  ↓
Future PAM integration
```

---

## Development setup

Create and activate a local Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Install dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Do not install Python dependencies globally.

Avoid:

```bash
sudo pip install ...
```

---

## Camera probe

Run from the repository root:

```bash
PYTHONPATH=src python -m faceauth.camera_probe
```

Expected output:

```text
Camera opened successfully
Resolution: 640x480
Frame captured: OK
```

---

## Face landmarks probe

The MediaPipe Face Landmarker model is required locally:

```text
models/face_landmarker.task
```

This file is intentionally ignored by Git.

Run:

```bash
PYTHONPATH=src python -m faceauth.landmarks_probe
```

Example output:

```text
Face detected | landmarks=478 | blendshapes=52 | frame=150
RESULT: OK - face detected in 87/150 frames
```

---

## Documentation

Project documentation is available in the GitHub Wiki.

Main pages:

- Home
- Fedora Setup
- Development Workflow
- Security Model

---

## Roadmap

### v0.1 - Camera and landmarks

- [x] Open webcam
- [x] Capture frame
- [x] Detect face landmarks
- [x] Enable blendshape output
- [ ] Estimate basic head direction

### v0.2 - Liveness challenge

- [ ] Look center
- [ ] Look left
- [ ] Look right
- [ ] Validate movement sequence

### v0.3 - Face enrollment

- [ ] Capture multiple samples
- [ ] Generate local face template
- [ ] Avoid raw image storage

### v0.4 - Face verification

- [ ] Compare current face with enrolled template
- [ ] Return CLI exit code
- [ ] Add configurable threshold

### v0.5 - PAM proof of concept

- [ ] Integrate with sudo only
- [ ] Keep password fallback
- [ ] Document rollback steps

---

## Security principles

This project follows these principles:

- do not store raw face images by default;
- keep password fallback mandatory;
- avoid root privileges during development;
- do not modify PAM until CLI verification is stable;
- use timeouts and attempt limits;
- log events, not biometric data;
- keep biometric templates local;
- document all security assumptions.

---

## License

This project is licensed under the Apache License 2.0.

See `LICENSE`.
