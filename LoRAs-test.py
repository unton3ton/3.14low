# python3 -m venv LORA
# source LORA/bin/activate
# pip install --upgrade pip


# https://huggingface.co/spaces/latent-consistency/super-fast-lcm-lora-sd1.5
# pip install diffusers==0.23.0
# pip install transformers

# https://pytorch.org/get-started/locally/
# pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
# pip install accelerate

'''
На базе Stable Diffusion энтузиасты собрали (https://twitter.com/abidlabs/status/1723074108739706959) модель, 
которая может генерировать изображения пока вы только набираете текст.

Был разработан новый метод увеличивающий скорость вывода в 10 раз. 
На видеокарте GeForce RTX 3090 генерация занимает 1 секунду. (https://t.me/black_triangle_tg)
'''

# deactivate

from diffusers import DiffusionPipeline, LCMScheduler

pipe = DiffusionPipeline.from_pretrained("Lykon/dreamshaper-7")#.to("cuda") 
pipe.scheduler = LCMScheduler.from_config(pipe.scheduler.config)
pipe.load_lora_weights("latent-consistency/lcm-lora-sdv1-5") #yes, it's a normal LoRA

results = pipe(
    prompt="Girl with a Pearl Earring in style starry night by Vincent van Gogh",
    num_inference_steps=4,
    guidance_scale=0.0,
)
results.images[0]

# prompt='Pixelart cat with a Pearl Earring in style starry night by Vincent van Gogh'
# prompt='Wanderer above the Sea of Fog in style starry night by Vincent van Gogh'