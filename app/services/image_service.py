from PIL import Image
from app.config import Config

class ImageService:
    @staticmethod
    def resize_image(image: Image.Image) -> Image.Image:
        """Resize image to maximum allowed dimensions."""
        image.thumbnail(Config.MAX_IMAGE_SIZE)
        return image

    @staticmethod
    def save_temp_image(image: Image.Image) -> str:
        """Save image to temporary file and return path."""
        image.save(Config.TEMP_IMAGE_PATH)
        return Config.TEMP_IMAGE_PATH
