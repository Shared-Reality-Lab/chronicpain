# AI Image Generation Workflow for Chronic Pain Art Therapy
This project includes the scripts for running the workflow for AI-guided image generation process components of the novel digital art therapy platform for chronic pain patients. 

## Requirements
found in requirements.txt 

## AI Terms/Usage 
img2img = image to image full transformation (input is an image, output is an entirely new image)
inpainting = image to image subsection transformation (input is an image and mask, output is the input image transformed only in the areas covered by the mask) 
NOTE: in all cases, the text prompt should be a description of the desired output (ex. for inpainting, the prompt is what the pixels covered by the mask should become)

## Details about each script 
AI_Pipeline_Components.py : Run this script to test out the inpainting or img2img functionality of Kandinsky 2.2 using your own images. 
1) Adjust the parameters under the section under the comment "#Image Generation Parameters" - prompt, input image, negative prompt, output file path, mask image if using inpainting
NOTE: the mask image must be white on black pixels 
2) Run the script, type 1 for img2img, 2 for inpainting - you should see a new output file in the path you designated 

SDXL_T2IAdapter.py : Run this script to test the ability of SDXL with its sketch-specialized T2I adapter in transforming a sketch to a high quality image using your own images. 
1) Adjust the parameters under the section under the comment "#Image Generation Parameters" - prompt, input image, negative prompt, output file path
2) Run the script - you should see a new output file in the path you designated 

GPT_Testing.py : Run this script to test the effects of using GPT 3.5 Turbo to change the user's natural description of their desired output into text more suitable as Kandinsky 2.2 text prompts.
1) Adjust the parameters in the section between the comments "#CHANGE BEFORE RUNNING#"
2) Run the script - you should see a new output file in the path you designated 
