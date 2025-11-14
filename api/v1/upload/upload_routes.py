import os
from flask import Blueprint, request
from api.utils.file_upload import allowed_file, unique_filename, UPLOAD_FOLDER
from .upload_controller import handle_upload

upload_bp = Blueprint('upload', __name__, url_prefix='/api/v1/upload')

@upload_bp.route('/', methods=['POST'])
def handle_file_upload():
  # Check if the post request has the file part
  if 'file' not in request.files:
      return 'No file part', 400

  file = request.files['file']
  return handle_upload(file)
