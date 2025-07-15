# 🧽 Resample Banding Fix – ComfyUI Node

A custom ComfyUI node that removes visible **banding artifacts** from latent images by reapplying a subtle diffusion pass using a low denoise value — preserving the original image while improving gradient quality.

---

## ✨ Features

- Fixes banding, posterization, and flat gradients
- Ultra-light resampling to keep pose and subject intact
- Supports multiple **samplers** and **schedulers**
- Ultra Fast with the fp8 version of Flux.1-Dev original
- Supersonic with Nunchaku chekpoint original
- Works especially well with models like FLUX

---
🖼 Example:
Before, After

<img width="2426" height="1232" alt="Capture d'écran 2025-07-15 002654" src="https://github.com/user-attachments/assets/7f574468-9d38-4ef2-b611-85229f3447ab" />


