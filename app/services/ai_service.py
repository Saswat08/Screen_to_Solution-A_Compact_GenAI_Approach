import os
import google.generativeai as genai
import markdown
from app.config import Config

class AIService:
    def __init__(self):
        genai.configure(api_key=Config.API_KEY)
        self.model = genai.GenerativeModel(Config.MODEL_NAME)
        self.markdown_converter = markdown.Markdown()

    def generate_response(self, image_path: str) -> str:
        """Generate AI response for the given image."""
        try:
            uploaded_file = genai.upload_file(image_path)
            prompt = self._get_prompt()
            result = self.model.generate_content([uploaded_file, prompt])
            return self.markdown_converter.convert(result.text)
        finally:
            if os.path.exists(image_path):
                os.remove(image_path)

    @staticmethod
    def _get_prompt() -> str:
        return (
            "\n\nYou are now integrated into an application that functions like an "
            "AI-based paint app. Anytime a user draws something, it usually is a "
            "problem. The image you received contains all details and values. Using "
            "the details, please deduce an answer and print the answer in markdown. "
            "Let the answer involve complete explanation."
        )
