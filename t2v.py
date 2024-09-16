from diffusers import TextToVideoZeroPipeline
import torch
import imageio


model_id = "stablediffusionapi/anime-diffusion"
pipe = TextToVideoZeroPipeline.from_pretrained(model_id, torch_dtype=torch.float16).to("cuda")

# Target 15 seconds at 15 FPS
# num_frames = 15 * 15  # 225 frames
prompt = "A man walks down the street and sees a cherry blossom tree"
result = pipe(prompt=prompt).images

# Convert frames to uint8 and save the video
result = [(r * 255).astype("uint8") for r in result]
imageio.mimsave("animated_video.mp4", result, fps=5)

print("Animated video saved as animated_video.mp4")
