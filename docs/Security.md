# Security model

## Principles

- Do not store raw face images by default.
- Store only local templates or embeddings.
- Keep password fallback.
- Avoid root privileges during development.
- Do not modify PAM until CLI verification is stable.
- Limit attempts.
- Use timeouts.
- Log events, not biometric data.

## Non-goals

This project does not claim to defeat:

- high-quality video replay attacks;
- deepfake attacks;
- infrared spoofing;
- compromised host systems.

## First safe target

The first authentication target will be `sudo`, not graphical login.
