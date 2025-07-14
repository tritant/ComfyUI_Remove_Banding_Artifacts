# 🧽 Resample Banding Fix – ComfyUI Node

A custom ComfyUI node that removes visible **banding artifacts** from latent images by reapplying a subtle diffusion pass using a low denoise value — preserving the original image while improving gradient quality.

---

## ✨ Features

- Fixes sky banding, posterization, and flat gradients
- Ultra-light resampling to keep pose and subject intact
- Supports multiple **samplers** and **schedulers**
- No prompt change required – reuses the original conditioning

---
