from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
#chat = client.chats.create(model="gemini-2.0-flash-preview-image-generation")
def drawImageTool (_input : str) -> list[str,BytesIO] :
    o = ["",None]
    response = client.models.generate_content(
    model="gemini-2.0-flash-preview-image-generation",
    contents=_input,
    config=types.GenerateContentConfig(
      response_modalities=['TEXT', 'IMAGE']
    )
)

    for part in response.candidates[0].content.parts:
        if part.text is not None:
            o[0] += part.text 
            print(f"response from VLM : {part.text}")
        elif part.inline_data is not None:
            o[1] = BytesIO(part.inline_data.data)
            image = Image.open(BytesIO((part.inline_data.data)))
            image.save('gemini-native-image.png')
            image.show()
    return o        

CreateImageFunc = {
    "name": "CreateImage",
    "description": "connects and sends a message to an API , which might return an image from the promt , and also include some text response",
    "parameters": {
        "type": "object",
        "properties": {
            "prompt": {
                "type": "string",
                "description": "the prompt for the model to draw the image",
            },
        },
        "required": ["prompt"],
    },
}

tools = tools = types.Tool(function_declarations=[CreateImageFunc])
config = types.GenerateContentConfig(tools=[tools])
contents = []
while True :
    contents.append(types.Content(parts=[types.Part(text=input("your turn : "))],role= "user"))
    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents= contents,
    config=config,
)
    if response.candidates[0].content.parts[0].function_call:
        function_call = response.candidates[0].content.parts[0].function_call
        print(f"Function to call: {function_call.name}")
        print(f"Arguments: {function_call.args}")
        if function_call.name == "CreateImage" :
            r = drawImageTool(function_call.args["prompt"])
            function_response_part = types.Part.from_function_response(
            name=function_call.name,
            response={"result": "response from the model : " + r[0] + "received an image " if r[1] != None else "no image received" },
            )
            contents.append(response.candidates[0].content) # Append the content from the model's response.
            contents.append(types.Content(role="user", parts=[function_response_part])) # Append the function response
            final_response = client.models.generate_content(
            model="gemini-2.0-flash",
            config=config,
            contents= contents,
            )
            print(final_response.text)

    else:
        print("No function call found in the response.")
        print(response.text)
