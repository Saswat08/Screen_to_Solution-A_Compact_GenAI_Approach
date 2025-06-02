import base64
import io
from PIL import Image

def process_base64_image(image_data: str) -> Image.Image:
    """Convert base64 string to PIL Image."""
    try:
        # Remove the data URL prefix
        image_data = image_data.split(",")[1]
        image_bytes = base64.b64decode(image_data)
        return Image.open(io.BytesIO(image_bytes))
    except Exception as e:
        raise ValueError(f"Failed to process image: {str(e)}") 