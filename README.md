# faceauth-linux

![Status](https://img.shields.io/badge/status-early%20prototype-orange)
![Platform](https://img.shields.io/badge/platform-Linux-blue)
![Primary target](https://img.shields.io/badge/primary%20target-Fedora-purple)
![Language](https://img.shields.io/badge/language-Python-yellow)
![Security](https://img.shields.io/badge/security-password%20fallback%20required-red)

Local face authentication prototype for Linux using facial landmarks, liveness checks and future PAM-ready verification.

> This project is experimental. It is not intended to replace passwords completely.

---

## Overview

`faceauth-linux` explores local face-based authentication for Linux systems.

The initial target is Fedora Linux, but the project is designed to remain generic enough for other Linux distributions.

The project is being developed incrementally:

1. camera access;
2. facial landmark detection;
3. basic head pose estimation;
4. liveness challenges;
5. face enrollment;
6. face verification;
7. optional PAM integration.

---

## Current status

Current milestone:

**v0.1 - Camera and landmarks**

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
