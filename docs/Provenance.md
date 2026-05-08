# Project Provenance

`faceauth-linux` is an independent project created as a personal software engineering and research-oriented portfolio project.

The codebase is developed independently and does not reuse private, institutional or proprietary source code.

## Purpose

The purpose of this project is to document and implement an incremental prototype for local Linux face authentication.

The project focuses on:

- camera access;
- facial landmark detection;
- head pose estimation;
- liveness validation;
- local face verification;
- Linux-friendly command line tooling;
- future PAM integration research.

## Development approach

The project follows an incremental development process.

Each major capability should be introduced through small, reviewable steps:

1. define the objective;
2. create or update an issue;
3. implement a minimal prototype;
4. test locally;
5. document known limitations;
6. commit with a clear message;
7. keep the main branch stable.

## Independence statement

This repository does not contain:

- private institutional code;
- proprietary datasets;
- confidential research material;
- unpublished third-party assets;
- biometric data from other people;
- raw face captures committed to version control.

Any third-party dependency, model or external reference should be documented explicitly.

## Data handling

The project must avoid committing:

- raw face images;
- camera captures;
- biometric templates;
- local model files;
- personal test data;
- credentials;
- system-specific secrets.

Local experimental data should remain outside version control.

## Research and portfolio intent

This project may be used as part of a technical portfolio or research preparation material.

The repository is intended to demonstrate:

- software engineering discipline;
- incremental development;
- security awareness;
- Linux development practices;
- computer vision experimentation;
- documentation quality;
- responsible handling of biometric-related software.

## Related future work

Future work may include:

- head pose estimation;
- liveness challenge validation;
- local face verification;
- configurable thresholds;
- Fedora-specific integration notes;
- PAM proof of concept;
- packaging experiments.
