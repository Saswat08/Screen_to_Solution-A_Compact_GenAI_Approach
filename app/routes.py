from flask import Blueprint, render_template, request, jsonify
from app.services.image_service import ImageService
from app.services.ai_service import AIService
from app.utils.image_utils import process_base64_image

bp = Blueprint('main', __name__)
ai_service = AIService()

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/submit', methods=['POST'])
def submit():
    try:
        # Get image data from request
        image_data = request.json.get('image')
        if not image_data:
            return jsonify(error="No image data provided"), 400

        # Process image
        image = process_base64_image(image_data)
        
        # Resize and save image
        image = ImageService.resize_image(image)
        temp_path = ImageService.save_temp_image(image)
        
        # Generate AI response
        response = ai_service.generate_response(temp_path)
        
        return jsonify(response=response)
    
    except ValueError as e:
        return jsonify(error=str(e)), 400
    except Exception as e:
        return jsonify(error="An unexpected error occurred"), 500
