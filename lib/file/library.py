class Library:

  def __init__(self, location):
    self.location = location
    self.library  = {}

  def simple_query(self, pattern):
    dirs  = os.listdir(self.location + pattern)
    files = map((lambda file: file.split('/')[-1]), dirs)
    return list(set(files))

  def file_objects(file):
    file_object = file_type(file)
    response = file_object.info
    if(file_object.valid_type()):
      return response

  def filter_items(item):
    if(item == None):
      return item

  def query(self, pattern, file_type):
    dirs = os.listdir(self.location + pattern)
    files = list(set(map(file_objects, dirs)))
    files = filter(filter_items, files)
    return files
