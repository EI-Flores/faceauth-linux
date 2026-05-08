# faceauth-linux

Local face authentication prototype for Linux using facial landmarks, liveness checks and PAM-ready verification.

## Goal

Build a local Linux authentication prototype that combines:

- facial landmarks;
- basic liveness detection;
- face verification;
- future PAM integration.

The project starts with Fedora Linux as the primary target.

## Current status

Early prototype.

Current milestone:

- [ ] Camera access
- [ ] Face landmark detection
- [ ] Head pose estimation
- [ ] Basic liveness challenge
- [ ] Face enrollment
- [ ] Face verification
- [ ] PAM integration
- [ ] Fedora packaging

## Security note

This project is experimental.  
It must not replace passwords completely.

Password fallback is mandatory.
