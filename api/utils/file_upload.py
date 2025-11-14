
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt'}
UPLOAD_FOLDER = 'static/uploads/'

def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()

def allowed_file(filename):
    # uncomment to see what the values are at any given point of execution
    # print(filename)
    # print(filename.rsplit("."))
    # print("what is this, rsplit", filename.rsplit(".")[-1])
    # print("what is this, split", filename.split(".")[-1])
    # print(filename.rsplit(".", 1))
    # print(filename.rsplit(".", 1)[0])
    # print(filename.rsplit(".", 1)[1])

    return '.' in filename and \
           get_file_extension(filename) in ALLOWED_EXTENSIONS

def unique_filename(filename):
    import uuid
    ext = get_file_extension(filename)
    return f"{uuid.uuid4().hex}.{ext}"



# allowed_file("cat_image.jpg")
# allowed_file("cat_image.multiple.jpg")
# allowed_file("cat_image.file.extensions.jpg")
# allowed_file("cat_image.jpg.is.this.real")
