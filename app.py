



import os
import time
import base64
import io
from flask import Flask, render_template, request, jsonify
from PIL import Image
import google.generativeai as genai
import markdown

# Configure the API
api_key = "AIzaSyBdDcD27Dxfgcd2apWbewdgFqQ3FEqoFGg"  # Replace with your actual API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    start_time = time.time()

    data = request.json
    image_data = data.get('image')

    # Process the image data
    image = process_image(image_data)

    # Upload the image and generate a response
    response = meow(image)

    print(f"Total time for submit: {time.time() - start_time:.2f} seconds")
    return jsonify(response=response)

def process_image(image_data):
    start_time = time.time()

    # Convert base64 string to a PIL Image
    image_data = image_data.split(",")[1]  # Remove the prefix
    image_bytes = base64.b64decode(image_data)

    # Load the image using PIL
    image = Image.open(io.BytesIO(image_bytes))
    return image

def meow(image):
    start_time = time.time()

    # Resize image before saving
    max_size = (1024, 1024)  # Set a maximum size for the image
    image.thumbnail(max_size)

    # Save the image to a temporary file if needed
    image_path = "temp_image.png"
    image.save(image_path)
    uploaded_file = genai.upload_file(image_path)
    
    prompt = "\n\nYou are now integrated into an application that functions like an AI-based paint app. " \
             "Anytime a user draws something, it usually is a problem. The image you received contains all " \
             "details and values. Using the details, please deduce an answer and print the answer in markdown. " \
             "Let the answer involve complete explanation."

    result = model.generate_content([uploaded_file, prompt])
    os.remove(image_path)

    md = markdown.Markdown()
    html = md.convert(result.text)
    return html

if __name__ == '__main__':
    app.run(debug=True)








