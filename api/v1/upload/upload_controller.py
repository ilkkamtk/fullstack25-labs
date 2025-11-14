import os
from api.utils.file_upload import allowed_file, unique_filename, UPLOAD_FOLDER

def handle_upload(file):
  # If user does not select file, browser may submit an empty part
  if file.filename == '':
      return 'No selected file', 400

  if file and allowed_file(file.filename):
      filename = unique_filename(file.filename)
      file.save(os.path.join(UPLOAD_FOLDER, filename))
      return 'File successfully uploaded', 200
