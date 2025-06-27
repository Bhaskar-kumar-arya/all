# [Scene 1 - Busy Jewellery Shop / Gold Buyer at Home]
# Voiceover: "Buying gold or silver? Staying updated on rates is everything."
# [Phone screen shows outdated metal rates on random websites — user frustrated.]

# [Scene 2 - Smooth transition to your app logo & clean UI]
# Voiceover: "Introducing [Your App Name], your one-stop solution for live metal rates and jewellery delivery."
# [App screen showing live gold, silver, platinum rates with sleek design.]

# [Scene 3 - Close-up of app features]

# Live Gold & Silver Prices — Updated Every Second

# Doorstep Jewellery Delivery — Trusted & Secure

# Voiceover: "Track real-time prices, place your jewellery orders, all from your phone."

# [Scene 4 - Happy user receiving jewellery at their doorstep]
# Voiceover: "From price-check to doorstep — simple, safe, smart."

# [Scene 5 - Final App Logo & Call to Action]
# Voiceover: "Download [Your App Name] now — Know the rates. Shop smart. Shine brighter."


prompt = """
a beautiful indian woman , wearing the ornament from the app, smiling elegantly, in a marriage event, with her husband , where her husband is looking 
"""


import os
import time
import base64
import google.genai as genai
from google.genai import types

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open("veoImage.jpg", "rb") as img_file:
    image_bytes = img_file.read()

# Base64URL encode the image bytes
encoded_image = base64.urlsafe_b64encode(image_bytes).decode("utf-8")

image_obj = types.Image(
    imageBytes=encoded_image,
    mimeType="image/jpeg"
)

operation = client.models.generate_videos(
    model="veo-2.0-generate-001",
    prompt=prompt,
    image=image_obj,
    config=types.GenerateVideosConfig(
        person_generation="allow_adult",
        aspect_ratio="16:9",
        number_of_videos=1
    ),
)

# Wait for videos to generate
while not operation.done:
    time.sleep(10)
    operation = client.operations.get(operation)

print(operation)
for n, video in enumerate(operation.response.generated_videos):
    fname = f'with_image_input{n}.mp4'
    print(fname)
    client.files.download(file=video.video)
    video.video.save(fname)
