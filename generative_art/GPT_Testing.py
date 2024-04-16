from diffusers import AutoPipelineForImage2Image
from diffusers.utils import load_image
import torch
from openai import OpenAI

#CHANGE BEFORE RUNNING#
use_gpt = False
input_image = load_image("Sketches/mthouse.jpg").resize((512, 512))
output_file_name = 'output21.jpg'
messages = [ {"role": "system", 
              "content":"You are an intelligent assistant helping the user write prompts to feed into kandinsky 2.2 image to image model. The user will tell you a description of what the output image shoud look like. You reply with a prompt user can feed into kandinsky 2.2 with no other characters."} ]
pt_prompt = "an image of a house and the house needs to be wooden and also i want the house to be in the alps like in between the mountains and the image needs to be realistic and i want a dog in front of the house too a golden retriever and the time should be winter"
negative_prompt = "error, low quality, mutilated, extra fingers, mutated hands, blurry, dehydrated, bad anatomy, bad proportions, extra limbs, disfigured, username, watermark, signature"
kandinsky_seed = 43 
kandinsky_strength = 0.5
GPT_temp = 0.1
GPT_seed = 43
#CHANGE BEFORE RUNNING#

client = OpenAI(api_key='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')

pipeline = AutoPipelineForImage2Image.from_pretrained("kandinsky-community/kandinsky-2-2-decoder", torch_dtype=torch.float16, use_safetensors=True)
pipeline.to("mps")
generator = torch.Generator(device="mps").manual_seed(kandinsky_seed)

if use_gpt: 
    messages.append( 
        {"role": "user", "content": pt_prompt}, 
    ) 
    chat = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=GPT_temp,
    seed=GPT_seed)
    gpt_reply = chat.choices[0].message.content  
    system_fingerprint = chat.system_fingerprint
    kandinsky_prompt = gpt_reply
else: 
    kandinsky_prompt = pt_prompt

print("Kandinsky 2.2 Prompt: ", kandinsky_prompt)
if use_gpt:
    print("Messages: ", messages)
    print("system_fingerprint: ", system_fingerprint)

image = pipeline(prompt=kandinsky_prompt, negative_prompt=negative_prompt, image=input_image, strength=kandinsky_strength, generator=generator).images[0]
image.save(output_file_name)
