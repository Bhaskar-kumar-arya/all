
prompt = """

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
