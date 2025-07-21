import torch
import comfy.samplers
from comfy.sample import prepare_noise
import random

class ResampleBandingFix:

    @classmethod
    def IS_CHANGED(self, **kwargs):
        return float("NaN")
        
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "latent": ("LATENT",),
                "model": ("MODEL",),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "denoise": ("FLOAT", {"default": 0.14, "min": 0.0, "max": 1.0, "step": 0.01}),
                "sampler": ([
                    "euler", "euler_ancestral", "dpmpp_2m", "dpmpp_2m_sde", "deis", "heun"
                ],),
                "scheduler": ([
                    "beta", "simple", "sgm_uniform", "karras", "exponential", "ddim_uniform",
                    "normal", "linear_quadratic", "kl_optimal"
                ],)
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "resample"
    CATEGORY = "latent/enhancement"
    DESCRIPTION = "🧽 Fix banding artifacts by re-sampling the latent with a low denoise strength."

    def resample(self, latent, model, positive, negative, denoise, sampler, scheduler):
        steps = 14  # Hardcoded
        # denoise = 0.14  # This is now an input
        cfg = 1.0  # Hardcoded
        seed = random.randint(0, 999_999_999)  # Hardcoded random seed

        latent_image = latent["samples"]
        device = latent_image.device

        start_step = int(steps * (1 - denoise))
        if start_step >= steps:
            start_step = steps - 1

        noise = prepare_noise(latent_image, seed)

        sampler_obj = comfy.samplers.KSampler(
            model,
            steps=steps,
            device=device,
            sampler=sampler,
            scheduler=scheduler,
            model_options=model.model_options
        )

        sigmas = sampler_obj.calculate_sigmas(steps)

        samples = sampler_obj.sample(
            noise=noise,
            positive=positive,
            negative=negative,
            cfg=cfg,
            latent_image=latent_image,
            start_step=start_step,
            last_step=steps,
            force_full_denoise=False,
            denoise_mask=None,
            sigmas=sigmas,
            callback=None,
            disable_pbar=False,
            seed=seed
        )

        samples = samples.to(device)
        output = latent.copy()
        output["samples"] = samples
        return (output,)

NODE_CLASS_MAPPINGS = {
    "ResampleBandingFix": ResampleBandingFix
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ResampleBandingFix": "🧽 Resample Banding Fix"
}