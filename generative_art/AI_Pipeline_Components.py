from diffusers import AutoPipelineForImage2Image, AutoPipelineForInpainting
from diffusers.utils import load_image
import torch
from PIL import ImageOps

#Image Generation Parameters
input_image = load_image("output2.jpg").resize((512, 512))
mask_image = ImageOps.invert((load_image("Mask/mthouse_mask.jpg").resize((512, 512))))
kandinsky_strength = 0.5
kandinsky_prompt = "patch of small flowers"
kandinsky_negative_prompt = "error, low quality, mutilated, extra fingers, mutated hands, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, disfigured, username, watermark, signature"
output_file_name = "output24.jpg"

#Loading Huggingface Pipelines
img2img_pipeline = AutoPipelineForImage2Image.from_pretrained("kandinsky-community/kandinsky-2-2-decoder", torch_dtype=torch.float16, use_safetensors=True)
img2img_pipeline.to("mps")

inpainting_pipeline = AutoPipelineForInpainting.from_pretrained("kandinsky-community/kandinsky-2-2-decoder-inpaint", torch_dtype=torch.float16)
inpainting_pipeline.to("mps")

generator = torch.Generator(device="mps")

#Functions for AI Pipeline Components 
def img2imge(img2img_pipeline, input_image, output_file_name, kandinsky_strength, kandinsky_prompt, kandinsky_negative_prompt):
    image = img2img_pipeline(prompt=kandinsky_prompt, negative_prompt=kandinsky_negative_prompt, image=input_image, strength=kandinsky_strength, generator=generator).images[0]
    image.save(output_file_name)

def inpainting(inpainting_pipeline, input_image, mask_image, output_file_name, kandinsky_strength, kandinsky_prompt, kandinsky_negative_prompt):
    image = inpainting_pipeline(prompt=kandinsky_prompt, negative_prompt=kandinsky_negative_prompt, image=input_image, mask_image=mask_image, strength=kandinsky_strength, generator=generator).images[0]
    image.save(output_file_name)

if __name__ == "__main__":
    choice = int(input("Which function would you like to run? 1 - img2img, 2-inpainting: "))
    if choice == 1:
        img2imge(img2img_pipeline, input_image, output_file_name, kandinsky_strength, kandinsky_prompt, kandinsky_negative_prompt)
    elif choice == 2:
        inpainting(inpainting_pipeline, input_image, mask_image, output_file_name, kandinsky_strength, kandinsky_prompt, kandinsky_negative_prompt)