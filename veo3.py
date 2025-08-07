import time
from google import genai
from google.genai import types
import os
import base64

client = genai.Client(api_key="AIzaSyBeISt0cP6XU8Mf1uiF8N5OnO-zczJHnjY")

with open("veo3.jpg", "rb") as img_file:
    image_bytes = img_file.read()

encoded_image = base64.urlsafe_b64encode(image_bytes).decode("utf-8")

image_obj = types.Image(
    imageBytes=encoded_image,
    mimeType="image/jpeg"
)

prompt = """this is a video showing how to search and download Arya alankar app on playstore and ios"'"""

operation = client.models.generate_videos(
    model="veo-3.0-generate-preview",
    prompt=prompt,
    image=image_obj
    )

# Poll the operation status until the video is ready.
while not operation.done:
    print("Waiting for video generation to complete...")
    time.sleep(10)
    operation = client.operations.get(operation)

# Download the generated video.
print(operation.response if operation.response else "")
generated_video = operation.response.generated_videos[0]
client.files.download(file=generated_video.video)
generated_video.video.save("dialogue_example.mp4")
print("Generated video saved to dialogue_example.mp4")


